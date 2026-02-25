class ValueError(Exception):
    pass


class BlockTranspositionCipher():

    def __init__(self, text, key, decrypt=False):
        self.text = text
        self.decrypt = decrypt
        self.key_check(key)
        key = key.lower()
        self.text_check(text)
        self.key_check(key)
        self.crypt_rules(key)
        self.crypt(key)

    def __iter__(self):
        return iter(self.encrypt_blocks)

    def crypt_rules(self, key):
        rules = {a: i for i, a in enumerate(sorted((key)))}
        self.rules = [rules[a] for i, a in enumerate((key))]
        if self.decrypt:
            for i, j in (list(zip(self.rules, [i for i in range(len(key))]))):
                self.rules[i] = j

    def text_check(self, text):
        if isinstance(text, str):
            return
        self.text = None

    def key_check(self, key):
        if not key.isalpha():
            raise ValueError(f"Key must contain only letters (a-z, A-Z). You`r key \"{key}\"")
        if len(key) != len(set(key)):
            raise ValueError(f"Key must consist of unique characters (no repeats). You`r key \"{key}\"")

    def split_into_blocks(self, key):
        key_len = len(key)
        self.text = self.text + " " * (key_len - (len(self.text) % key_len))
        return [self.text[i: i + key_len] for i in range(0, len(self.text) - key_len + 1, key_len)]

    def crypt(self, key):
        result = []
        for block in (self.split_into_blocks(key)):
            result.append(''.join([block[i] for i in self.rules]))
        self.encrypt_blocks = result
        if self.decrypt:
            if self.encrypt_blocks[-1].isspace() or not self.encrypt_blocks[-1]:
                self.encrypt_blocks.pop(-1)
            self.encrypt_blocks[-1] = self.encrypt_blocks[-1].rstrip()
            print(len(self.encrypt_blocks[-1]))
        self.text = "".join(self.encrypt_blocks)
