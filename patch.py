from pathlib import Path

file_path = Path("app/build.gradle")

old = """dependencies {
}"""

new = """dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
}"""

content = file_path.read_text()

count = content.count(old)

if count == 1:
    file_path.with_suffix(".bak").write_text(content)
    content = content.replace(old, new)
    file_path.write_text(content)
    print("OK")
else:
    print(f"FAIL: trouvé {count}")
