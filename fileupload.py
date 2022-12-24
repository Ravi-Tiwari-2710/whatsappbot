import requests
test_file = open("Ravi_RESUME.pdf", "rb")
test_url = "http://httpbin.org/post"
test_response = requests.post(test_url, files = {"form_field_name": test_file})
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")