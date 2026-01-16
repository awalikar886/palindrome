def palindrome(text):
  if text==text[::-1]:
    result = (
        f"text: {text}\n"
    )

    return result


if __name__ == "__main__":
    print(palindrome("madam"))
