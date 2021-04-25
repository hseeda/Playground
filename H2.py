# from pathlib import Path
# path = '.'
# for path in Path(path).iterdir():
#     print(path)



# from pathlib import Path
# path = Path('.')
# dirs = [e for e in path.iterdir() if e.is_dir()]

# for dir in dirs:
#     print(dir)
#     # print(dir.parts[-1])

# from pathlib import Path
# home_path = Path.home()
# print(*Path(home_path).iterdir(), sep="\n")

# from pathlib import Path
# path = Path('.')
# for e in path.glob('*.py'):
#     print(e)


from pathlib import Path
path = Path('.')
for e in path.rglob('*.py'):
    print(e)
    