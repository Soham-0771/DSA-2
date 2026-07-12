class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        return sorted(count, key=lambda word: (-count[word], word))[:k]