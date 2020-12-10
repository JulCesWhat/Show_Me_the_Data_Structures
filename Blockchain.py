import hashlib
import datetime


class BlockChain:
    def __init__(self, block=None):
        self.block = block
        self.current_block = block
        self.length = 0

    def append(self, data):
        time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        if self.block is None:
            self.block = Block(time, data, None)
            self.current_block = self.block
        else:
            self.current_block.next_val = Block(time, data, self.current_block.hash)
            self.current_block = self.current_block.next_val

    def get_block_at_position(self, position):
        current_pos = 0
        local_current_block = self.block
        while position is not current_pos:
            local_current_block = local_current_block.next_val
            current_pos += 1

        if current_pos is not position:
            return None
        else:
            return local_current_block


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_val = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


if __name__ == "__main__":
    block_chain = BlockChain()
    block_chain.append("First block")
    block_chain.append("Second block")
    block_chain.append("Third block")
    block_chain.append("Fourth block")
    block_chain.append("Fifth block")
    block_chain.append("Sixth block")

    item_pos_1 = block_chain.get_block_at_position(1)
    print(item_pos_1.data)
    item_pos_2 = block_chain.get_block_at_position(2)
    print(item_pos_2.data)
    item_pos_0 = block_chain.get_block_at_position(0)
    print(item_pos_0.data)
