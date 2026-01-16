def palindrome(text):
  if text==text[::-1]:
    (
    print("palindrome")
  else:
    print("not palindrome"))
    result = (
        f"text: {text}\n"
    )

    return result


if __name__ == "__main__":
    print(palindrome("madam"))
