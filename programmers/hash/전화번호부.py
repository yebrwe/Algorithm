def solution(phone_book):
    phone_book = sorted(phone_book)

    for i, p in enumerate(phone_book):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
print(solution(["119", "97674223", "1195524421"]))