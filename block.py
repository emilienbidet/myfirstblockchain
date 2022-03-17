import hashlib


class Block:
    def __init__(self, timestamp="", data=[]):
        self.timestamp = str(timestamp)
        self.data = data
        self.previous_hash = ""
        self.nonce = 0
        self.hash = self.get_hash()

    def get_hash(self):
        sha = hashlib.sha256()
        hash_str = (
            self.previous_hash + self.timestamp + str(self.data) + str(self.nonce)
        )
        sha.update(hash_str.encode("utf-8"))
        return sha.hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.get_hash()
        print("Block mined: " + self.hash)

    def __str__(self):
        return (
            "Block Hash: "
            + self.hash
            + "\n"
            + "Previous Hash: "
            + self.previous_hash
            + "\n"
            + "Timestamp: "
            + self.timestamp
            + "\n"
            + "Data: "
            + str(self.data)
        )
