li_1 = {
    "A": "가", "B": "나", "C": "다", "D": "라", "E": "마", "F": "바",
    "G": "사", "H": "아", "I": "자", "J": "차", "K": "카", "L": "타",
    "M": "파", "N": "하", "O": "거", "P": "너", "Q": "더", "R": "러",
    "S": "머", "T": "버", "U": "서", "V": "어", "W": "저", "X": "처",
    "Y": "커", "Z": "터",
    "a": "고", "b": "노", "c": "도", "d": "로", "e": "모", "f": "보",
    "g": "소", "h": "오", "i": "조", "j": "초", "k": "코", "l": "토",
    "m": "포", "n": "호", "o": "구", "p": "누", "q": "두", "r": "루",
    "s": "무", "t": "부", "u": "수", "v": "우", "w": "주", "x": "추",
    "y": "쿠", "z": "투",
    "0": "기", "1": "니", "2": "디", "3": "리", "4": "미",
    "5": "비", "6": "시", "7": "이", "8": "지", "9": "치"
}

li_1_extended = {}
for k, v in li_1.items():
    li_1_extended[k.upper()] = v
    li_1_extended[k.lower()] = v

li_2 = {v: k for k, v in li_1_extended.items()}

li_2_extended = {}
for k, v in li_2.items():
    li_2_extended[k] = v
    li_2_extended[k.upper()] = v

mode = input("작업을 선택하세요 (e: 복호화 / r: 복호화키 해독): ").strip().lower()

if mode == "e":
    user_input = input("암호문을 입력하세요: ")
    def caesar_shift(text, shift):
        shifted = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                shifted += chr((ord(ch) - base + shift) % 26 + base)
            else:
                shifted += ch
        return shifted

    def complex_decode(text):
        reversed_text = text[::-1]
        shifted_text = caesar_shift(reversed_text, -2)
        result = []
        i = 0
        while i < len(shifted_text):
            chunk = shifted_text[i:i+2]
            if chunk in li_1:
                result.append(li_1[chunk])
                i += 2
            else:
                ch = shifted_text[i]
                if i % 2 == 0:
                    result.append(li_1.get(ch, "?"))
                else:
                    result.append(li_1_extended.get(ch, "?"))
                i += 1
        return "".join(result)

    result = complex_decode(user_input)
    print("복호화 결과:", result)


elif mode == "r":
    user_input = input("복호화된 한글을 입력하세요: ")
    encoded = "".join([li_2_extended.get(char, "?") for char in user_input])
    def caesar_shift(text, shift):
        shifted = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                shifted += chr((ord(ch) - base + shift) % 26 + base)
            else:
                shifted += ch
        return shifted
    reversed_encoded = caesar_shift(encoded, 2)[::-1]
    print("원래 암호문:", reversed_encoded)

else:
    print("잘못된 입력입니다. 'e', 'c', 'r' 중 하나를 입력하세요.")