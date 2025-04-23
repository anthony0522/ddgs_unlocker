import time

from src.ddgUnlocker import ddgsUnlocker

if __name__ == '__main__':
    print('ddgUnlocker started')
    while True:
        try:
            unlocker = ddgsUnlocker()
            unlocker.ddg_search()
            unlocker.quit()
            print("Search completed successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(1)