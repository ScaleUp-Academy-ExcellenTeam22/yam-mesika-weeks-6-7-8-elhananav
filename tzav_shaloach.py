class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'read': False,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, N=0):
        """Returns the messages in the user's inbox

        :param str username: The username whose messages will be returned
        :param int N: Number of massages to be returned. If not delivered return all inbox massages
        :return: List of all unread massages
        """
        massage_amount = N if N != 0 and N < len(self.boxes[username]) else len(self.boxes[username])
        return_massages = [massage for massage in self.boxes[username][:massage_amount] if massage['read'] is False]
        for i in range(0, len(return_massages)):
            self.boxes[username][i]['read'] = True
        return return_massages

    def search_inbox(self, username, sentence):
        """Return massages that contain a certain sentence

        :param sentence: Sentence that the massage containing
        :param username: The username whose messages will be searched
        :return: List of all massages that contain a certain sentence
        """
        return [massage for massage in self.boxes[username] if sentence in massage['body']]