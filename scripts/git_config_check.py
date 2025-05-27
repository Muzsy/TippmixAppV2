import subprocess
import sys

def check_remote():
    result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        print("❌ Nincs beállított Git távoli tároló (remote).\nFuttasd: git remote add origin <url>")
        return False
    print("✅ Git remote be van állítva:")
    print(result.stdout)
    return True

def check_upstream():
    result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ A jelenlegi ág nincs összekötve a távoli ággal (upstream missing).\nFuttasd: git push --set-upstream origin main")
        return False
    print(f"✅ Upstream be van állítva: {result.stdout.strip()}")
    return True

def check_status():
    result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  Vannak nem commitált változások:")
        print(result.stdout)
        return False
    print("✅ Nincsenek nem commitált változások.")
    return True

def check_push():
    print("🚀 Git push teszt (dry-run)...")
    result = subprocess.run(["git", "push", "--dry-run"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ A push parancs nem sikerülne. Részletek:")
        print(result.stderr)
        return False
    print("✅ Push működne (dry-run alapján).")
    return True

def main():
    print("🔍 Git konfiguráció ellenőrzése...\n")
    ok = True
    if not check_remote():
        ok = False
    if not check_upstream():
        ok = False
    if not check_status():
        ok = False
    if not check_push():
        ok = False

    if not ok:
        print("\n🔴 Hibák a Git konfigurációban. Javítsd őket a generálás előtt!")
        sys.exit(1)
    else:
        print("\n🟢 Git konfiguráció rendben van. Mehet a generálás.")

if __name__ == "__main__":
    main()
