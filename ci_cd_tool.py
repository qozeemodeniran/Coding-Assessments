import time

def build():
    print("[Build] building started...")
    time.sleep(2)
    print("[Build] building completed.")

def test():
    print("[Test] testing started...")
    time.sleep(1)
    print("[Test] testing completed.")

def deploy():
    print("[Deploy] deploying started...")
    time.sleep(3)
    print("[Deploy] deploying completed.")

if __name__ == "__main__":
    try:
        build()
        test()
        deploy()
        print("CI/CD pipeline executed successfully.")

    except Exception as e:
        print(f"CI/CD pipeline failed. Error: {e}")