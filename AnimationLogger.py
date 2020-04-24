from lib.Message import MessageType

'''
    Responsible for periodically checking what messages have been sent in the past interval. 
    Takes messages and combines them into a DataFrame and attaches it to the global log. 
'''

class AnimationLogger:

    def __init__(self, instance):
        self.G = instance.G
        self.env = instance.env
        self.holder = instance.initialHolderNum
        self.log = []

    def log_update(self, msg_log):
        old_messages = []

        while True:
            new_messages = []
            message_history = []
            previous_time = self.env.now
            # Add all messages that have just been sent to the queue
            yield self.env.timeout(0.01)

            while len(msg_log) > 0:

                msg = msg_log.pop(0)
                message_history.append(msg)

                if msg.message_type != MessageType.pass_key and msg.message_type != MessageType.resource_request:
                    msg.trans_time = 1

                new_messages.append(msg)

            # Remove messages from the queue that have reached their destination
            for msg in old_messages:
                if msg.time_sent <= self.env.now - msg.trans_time:
                    old_messages.remove(msg)

            old_messages = old_messages + new_messages
            self.log.append(DataFrame(old_messages, self.G.copy(), message_history))


class DataFrame:

    def __init__(self, message_log, graph_instance, message_history):
        self.message_log = message_log
        self.graph_instance = graph_instance
        self.message_history = message_history
