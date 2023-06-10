import asyncio

async def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = await file.read()
            return contents
    except FileNotFoundError:
        return None

async def write_file(filename, contents):
    try:
        with open(filename, 'w') as file:
            await asyncio.to_thread(file.write, contents)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu do pliku: {e}")

async def main():
    filename = 'example.txt'
    contents = 'Przykładowa zawartość pliku.'

    read_task = asyncio.create_task(read_file(filename))
    read_contents = await read_task

    if read_contents is not None:
        print(f"Zawartość pliku '{filename}': {read_contents}")
    else:
        print(f"Plik '{filename}' nie został znaleziony.")

    write_task = asyncio.create_task(write_file(filename, contents))
    await write_task
    print(f"Plik '{filename}' został zapisany.")

asyncio.run(main())