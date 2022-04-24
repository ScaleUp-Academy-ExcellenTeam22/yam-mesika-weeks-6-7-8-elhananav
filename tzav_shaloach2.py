class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
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
        Message.ID += 1
        message_details = Message(Message.ID, sender, message_body)
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return message_details.id

    def read_inbox(self, username, N=0):
        """Returns the messages in the user's inbox

        :param str username: The username whose messages will be returned
        :param int N: Number of massages to be returned. If not delivered return all inbox massages
        :return: List of all unread massages
        """
        massage_amount = N if N != 0 and N < len(self.boxes[username]) else len(self.boxes[username])
        return_massages = [massage for massage in self.boxes[username][:massage_amount] if massage.read is False]
        for i in range(0, len(return_massages)):
            self.boxes[username][i].read = True
        return return_massages

    def search_inbox(self, username, string):
        return [massage for massage in self.boxes[username] if string in massage.body]


class Message:
    """A Message class. Allows creating messages in which can be sent to each other.

    :ivar int ID: Incremental id of the last message.
    :ivar int id: Id of the message.
    :ivar str sender: Name of the message sender.
    :ivar str body: The body of the message

    :param int id: Id of the message.
    :param str sender: Name of the message sender.
    :param str body: The body of the message
    """

    ID = 0

    def __init__(self, id, sender, body):
        self.id = id
        self.sender = sender
        self.body = body
        self.read = False

    def __str__(self):
        return f"message id: {self.id} sent from: {self.sender} is: \n{self.body}"

    def __len__(self):
        return len(self.body)
