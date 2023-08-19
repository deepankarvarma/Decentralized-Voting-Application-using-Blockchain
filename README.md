# Decentralized Voting Application using Blockchain

This repository contains a simple implementation of a decentralized voting application using blockchain technology. The application is built in Python and utilizes the hashlib library for hashing and time for timestamp generation.

## How It Works

The decentralized voting application consists of several main components: Blocks, Blockchain, Voters, and the VotingApp.

### 1. Block Class Definition

The `Block` class represents a block in the blockchain. It contains the following attributes:

- `index`: The index of the block in the chain.
- `previous_hash`: The hash of the previous block.
- `timestamp`: The timestamp of when the block was created.
- `data`: The data contained in the block, which in this case represents voting information.
- `hash`: The hash value of the block calculated based on its attributes.

### 2. Blockchain Class Definition

The `Blockchain` class manages the chain of blocks. It includes methods to create the genesis block and add new blocks to the chain. The blockchain is initialized with a genesis block, and subsequent blocks are added as new votes are cast.

### 3. Voter Class Definition

The `Voter` class represents a voter in the system. Each voter is identified by a unique `voter_id` and tracks whether they have cast a vote.

### VotingApp

The `VotingApp` class ties everything together. It maintains a blockchain and a dictionary of registered voters. The methods in this class allow users to register voters, cast votes, and retrieve vote counts.

## Example Usage

Here's an example of how to use the `VotingApp` to simulate a voting process:

```python
# Create a VotingApp instance
voting_app = VotingApp()

# Register voters
voting_app.register_voter("voter1")
voting_app.register_voter("voter2")

# Cast votes
voting_app.cast_vote("voter1", "Candidate A")
voting_app.cast_vote("voter2", "Candidate B")
voting_app.cast_vote("voter2", "Candidate B")

# Get vote counts
print("Vote Count for Candidate A:", voting_app.get_vote_count("Candidate A"))
print("Vote Count for Candidate B:", voting_app.get_vote_count("Candidate B"))
```

