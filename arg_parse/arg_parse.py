import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('name', nargs='?')
    args = ap.parse_args()
    name = (args.name or 'World')
    print("Hello,", name, "!")
