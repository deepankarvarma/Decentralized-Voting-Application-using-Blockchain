import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, '0', int(time.time()), 'Genesis Block', 'genesis_hash')
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        hash = self.calculate_hash(index, previous_hash, timestamp, data)
        
        new_block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f'{index}{previous_hash}{timestamp}{data}'.encode()
        return hashlib.sha256(value).hexdigest()

class Voter:
    def __init__(self, voter_id):
        self.voter_id = voter_id
        self.voted = False

class VotingApp:
    def __init__(self):
        self.blockchain = Blockchain()
        self.voters = {}

    def register_voter(self, voter_id):
        if voter_id not in self.voters:
            self.voters[voter_id] = Voter(voter_id)
            return True
        return False

    def cast_vote(self, voter_id, candidate):
        if voter_id in self.voters and not self.voters[voter_id].voted:
            self.voters[voter_id].voted = True
            data = f"Vote: {candidate}"
            self.blockchain.add_block(data)
            return True
        return False

    def get_vote_count(self, candidate):
        count = 0
        for block in self.blockchain.chain:
            if f"Vote: {candidate}" in block.data:
                count += 1
        return count

# Example usage
voting_app = VotingApp()
voting_app.register_voter("voter1")
voting_app.register_voter("voter2")
voting_app.cast_vote("voter1", "Candidate A")
voting_app.cast_vote("voter2", "Candidate B")
voting_app.cast_vote("voter2", "Candidate B") # # This vote will be rejected since voter2 already voted
print("Vote Count for Candidate A:", voting_app.get_vote_count("Candidate A"))
print("Vote Count for Candidate B:", voting_app.get_vote_count("Candidate B"))
