from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def main():
    while True:
        mode = input("모드 선택 (a: AES 암호화, d: AES 복호화, q: 종료): ").strip().lower()
        if mode == "q":
            print("프로그램을 종료합니다.")
            break
        elif mode == "a":
            key = get_random_bytes(16)  # 128-bit AES 키
            plain_text = input("암호화할 한글 문자열을 입력하세요: ")

            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(plain_text.encode("utf-8"), AES.block_size))

            encoded_cipher = base64.b64encode(cipher.iv + ct_bytes).decode("utf-8")
            encoded_key = base64.b64encode(key).decode("utf-8")

            print("암호문:", encoded_cipher)
            print("복호화를 위한 키:", encoded_key)
        elif mode == "d":
            encoded_cipher = input("암호문을 입력하세요: ")
            encoded_key = input("AES 키를 입력하세요: ")

            raw_data = base64.b64decode(encoded_cipher)
            key = base64.b64decode(encoded_key)
            iv = raw_data[:16]
            ct = raw_data[16:]

            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size).decode("utf-8")

            print("복호화 결과:", pt)
        else:
            print("지원하지 않는 모드입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()