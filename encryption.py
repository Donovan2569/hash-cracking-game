import json
import hashlib

def compute_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

# Load the original JSON data (which should have "easy", "medium", "hard" keys)
with open('./.wordlists/hash_challenges.json', 'r') as f:
    data = json.load(f)

# Load plaintext words for each difficulty
with open('./.wordlists/easy.txt', 'r') as f:
    easy_words = f.read().splitlines()
with open('./.wordlists/medium.txt', 'r') as f:
    medium_words = f.read().splitlines()
with open('./.wordlists/hard.txt', 'r') as f:
    hard_words = f.read().splitlines()

# Your hints data, aligned with each word by index (example placeholders)
easy_hints = [
    "A common fruit often red or green, keeps the doctor away.",
    "A big striped wild cat from Asia.",
    "A sour yellow citrus fruit.",
    "A juicy fruit with fuzzy skin.",
    "A tropical stone fruit, sweet and orange inside.",
    "Small, juicy fruits like strawberries or blueberries.",
    "A large bird of prey known for keen eyesight.",
    "A citrus fruit and a color.",
    "Small round fruit used to make wine.",
    "Where people live.",
    "A natural flowing watercourse.",
    "White or gray fluffy formations in the sky.",
    "A small piece of rock.",
    "The color of grass and leaves.",
    "The color of the sky on a clear day."
]

# Add hints for medium and hard similarly:
medium_hints = [
    "A secret key to access accounts.",
    "Bright light from the sun.",
    "A common simple password phrase.",
    "Mythical fire-breathing creature.",
    "Popular sport played with a round ball.",
    "A primate known for swinging in trees.",
    "The standard keyboard layout.",
    "A common password phrase expressing affection.",
    "A sport with a bat and ball played on a diamond.",
    "A dark shape cast by an object blocking light.",
    "The power or right to act freely.",
    "One who has control or expertise.",
    "A friendly greeting combined with numbers.",
    "A polite greeting for guests.",
    "A simple username/password combo."
]

hard_hints = [
    "Phrase popularized by a video game, means deception.",
    "A phrase meaning 'trust no one.'",
    "Part of a famous password phrase.",
    "Polite way of asking for access.",
    "An affectionate, long password phrase.",
    "Something highly confidential.",
    "A compound word plus numbers.",
    "A nickname for a famous comic book hero.",
    "Famous phrase from a fantasy series.",
    "A classic fairy tale character.",
    "Someone who keeps watch overnight.",
    "A colorful insect.",
    "A soft, quiet sound.",
    "A mysterious place in Superman comics.",
    "A phrase meaning endless illumination."
]

def update_section(section_name, words, hints):
    updated_list = []
    for i, word in enumerate(words):
        updated_list.append({
            "hash": compute_md5(word),
            "algorithm": "md5",
            "hint": hints[i] if i < len(hints) else ""
        })
    data[section_name] = updated_list

# Update all three sections
update_section("easy", easy_words, easy_hints)
update_section("medium", medium_words, medium_hints)
update_section("hard", hard_words, hard_hints)

# Write to a new JSON file
with open('updated_hashchallenges.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Updated JSON with MD5 hashes and hints saved to 'updated_hashchallenges.json'.")
