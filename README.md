
# 🧱 Minimal Python Blockchain

A minimal blockchain implementation written in Python to demonstrate how blockchains work at a fundamental level.
It shows how cryptography, mining, and validation combine to create a tamper-resistant ledger—using only standard Python tools.


---

## 📌 What This Project Teaches

- How blocks are built  
- How to create unique fingerprints for blocks (hashing)  
- How mining works with hard math problems  
- How to check if blocks are real  
- How to start a new blockchain (genesis block)  
- Ideas used in real blockchains like Bitcoin  

---

## 📂 Project Structure

```

blockchain/
│
├── blockchain.py
└── README.md

```

---

## 📦 Block Structure

Each block is represented by the `Block` class and consists of the following fields:

| Field | Description |
|------|-------------|
| `index` | Position of the block in the blockchain |
| `nonce` | Counter used for Proof-of-Work |
| `timestamp` | Time at which the block was created |
| `data` | Arbitrary payload / transaction data |
| `prev_hash` | Hash of the previous block |
| `hash` | SHA-256 hash of the current block |

A hash is like a unique fingerprint for a block.  
If you change even one tiny thing, the fingerprint changes completely.

---

## 🔗 Hash Calculation

The hash is calculated by concatenating the following fields into a single string:

```

index + nonce + timestamp + data + previous_hash

````

This string is then:
1. Converted to bytes  
2. Hashed using SHA-256  
3. Converted to a hexadecimal string  

```python
hashlib.sha256(encoded_block_bytes).hexdigest()
````

SHA-256 always gives the same answer for the same input, and two different inputs will never give the same answer. That's why it's perfect for protecting blockchains.

---

## ⛏️ Proof-of-Work (PoW)

This blockchain uses Proof-of-Work to make creating blocks hard and stopping cheaters expensive.

### Difficulty Rule

A block is good only if its fingerprint (hash) starts with:

```
0000
```

This rule makes mining hard.

---

### 🛠️ Mining Process

Mining is performed inside the `calculate_hash()` method:

1. Start with `nonce = 0`
2. Compute the block hash
3. If the hash does not satisfy the difficulty condition:

   * Increment the nonce
   * Recalculate the hash
4. Repeat until a valid hash is found

```python
while True:
    #Making a string for hashing
    block_hash_string = f"{self.index}{self.nonce}{self.timestamp}{self.data}{self.previous_hash}"

    #Converting the hash string into a bytes object
    encoded_block_bytes = block_hash_string.encode()

    hash_string = hashlib.sha256(encoded_block_bytes).hexdigest()

    if hash_string.startswith("0000"):
        return hash_string
    self.nonce +=1
```

This takes a lot of computer power on purpose—it's meant to be hard.

---

## 🔐 Why Proof-of-Work Matters

* Stops people from creating blocks too easily
* Makes cheating very expensive (lots of computer work)
* If someone cheats, they have to redo all future blocks too
* Protects the blockchain through hard math, not trust

---

## 🛡️ Validation & Tamper Detection

We check if blocks are real and honest using a checker function.

A block is real only if all four of these are true:

1. **Blocks Are In Order**

```
block number > previous block number
```

2. **Mining is Proof**

```
block fingerprint starts with 0000
```

3. **Chain Link Check**

```
block points to previous block's fingerprint
```

4. **Time Moves Forward**

```
this block's time > previous block's time
```

These checks ensure the chain cannot be modified without detection.

---

## 🚨 How Tampering Is Detected

If someone tries to cheat by changing:

* Block data
* When it was made
* Mining counter
* Link to previous block

This happens:

* The block's fingerprint changes
* The next block no longer points to it
* The mining proof fails

Now the chain is broken. To cheat, they'd have to redo all future blocks too—too hard!

---


## 🧬 Initialising a Blockchain

This is done when an object of BlockChain class is created by calling the `__init__()` function automatically.

```python
class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.construct_genesis()
```

It initialises the chain list which is essentially the block chain storing all the blocks, the current data list which stores the data required for a particular block creation. It also calls a method `construct_genesis()` for creating a genesis block to start the blockchain.





---


## ➕ Add Block

The method to create and append a new Block, in the Block Chain:

```python
add_block(self,previous_hash,data)
```

It takes inputs as previous hash and data for the block to be created, calculates the hash using SHA-256 algorithm and does proof of work by using `calculate_hash()` method. Finally it initializes current_data to empty list and appends the new block to the chain list.



---

## 🌱 Genesis Block

The blockchain begins with a Genesis Block, created automatically:

```python
self.add_block(prev_hash="0000", data=self.current_data)
```

The Genesis Block acts as the root of trust for the entire blockchain.


---

## ✅ What I have Learned

* How to lock data safely with math (SHA-256)
* How mining works with guess-and-check
* How to catch cheaters by linking fingerprints
* A simple, clear design anyone can understand

This project provides a strong conceptual foundation for understanding how real-world blockchains operate.

---








