import argparse
import shutil
import subprocess
import sys
import threading
import time
from typing import List

GREEN = "\033[92m"
RESET = "\033[0m"

FRIDA_CODESHARES = [
    "enovella/anti-frida-bypass",
    "fdciabdul/frida-multiple-bypass",
    "sowdust/universal-android-ssl-pinning-bypass-2",
    "licitrasimone/flutter-ssl-pinning-bypass",
    "pcipolloni/universal-android-ssl-pinning-bypass-with-Frida",
    "akabe1/frida-multiple-unpinning",
    "masbog/frida-android-unpinning-ssl",
    "TheDauntless/disable-flutter-tls-v1",
    "hyugogirubato/android-native-interceptor",
    "segura2010/android-certificate-pinning-bypass",
    "Q0120S/bypass-ssl-pinning",
    "pbalmelle/android-ssl-bypass",
    "fahad-source/frida-combined-bypass--anti-root--flutter-tls-pinning",
    "jerry/ultimate-combined-bypass",
    "RohindhR/react-native-jail-monkey-bypass-all-checks",
    "007panda/unpinning",
    "meerkati/universal-android-debugging-bypass",
    "kooroshh/ssl-pinning-bypass-okhttp4",
    "avltree9798/universal-android-ssl-pinning-bypass",
    "SahilH4ck4you/https-traffic-interception--bypss-okhttp3certificatepinner-android-trustmanagerimpl-sslcontext-hostnameverifier",
    "dodal-omkar/sslslayer",
    "dodal-omkar/sslslayerv3",
    "gru122121/okhttp3-logger",
    "vichhka-git/android-multiple-pinning-bypass",
    "jerry/final-ultimate-bypass-avinash",
    "ssecurityy/universal-robust-advanced-root--ssl-pinning-bypass",
    "beta0x01/ssl",
    "x90nopslide/conscrypt-ssl-bypass",
    "x90nopslide/anti-frida-bypass",
    "kushjasrapuria/conscrypt-ssl-bypass",
    "kushjasrapuria/anti-frida-bypass",
    "sahabrifki/okhttp3-obfuscated---ssl-pinning-bypass",
    "h4rithd/onerule-by-h4rithd",
    "teknogeek/android-universal-ssl-unpin",
    "Linuxinet/frida-traffic-interceptor",
    "ercu/root-and-bypass-ssl",
    "vadim-a-yegorov/universalunpinner",
    "ivan-sincek/android-ssl-pinning-bypass",
    "nneonneo/android-okhttp3-logger",
    "0xbad0c0d3/okhttp-proxy-installator",
    "federicodotta/okhttp3-pinning-bypass",
    "silva95gustavo/okhttp3-certificate-pinner-bypass",
    "masihyeganeh/re",
    "voltagex/fiddler-4-ssl-pinning-bypass",
    "mrmacete/uiwebview-ssl-validation-killer",
    "SahilH4ck4you/android-ssl-pinning--and-devloper-options-bypass-",
    "jorgenytterstad/check2",
    "jorgenytterstad/check1",
    "AamishBaig/script4",
    "krapgras/frida-ios-cipher-updated-for-frida-17",
    "realkerberos1/ssl-unpinning",
    "realkerberos1/okhttp3-bypass",
    "paragbagul111/android-proxy-detection-bypass-and-traffic-forwarding",
    "sv110040/universal-android-security-bypass-root--ssl--play-protect",
    "sv110040/play-protect-integrity-bypass",
    "rustyrend107/androidsslunpinning",
    "rustyrend107/rusty",
    "jadkorr/android-flutter-bypass",
    "realkerberos1/android-bypass-ssl",
    "melanie.valentetransp/arabe-all-bypass",
    "jadkorr/universal-ssl-pinning-bypass",
    "latestnew1310/root-ssl-bypaxx-check",
    "latestnew1310/final-ultimate-bypass-avinash",
    "latestnew1310/ultimate-combined-bypass",
    "aiexz/react-native-android-js-execution",
    "sanmeetpannu/advance-ssl-unpinning",
    "realkerberos1/ssl-pinning-bypass-v2",
    "dontlosecontrol/okhttp4bypass",
    "skytolfers/flutter-ssl-pinning-bypass",
    "h4rithd/jailmonkey-bypass",
    "zenlykoi/bypass-ssl-pinning",
    "RadonCoding/frida-okhttp3-tls",
    "RadonCoding/frida-okhttp3-intercept",
    "Akramelbahar/native-request-module-offset-finder-",
    "paragbagul111/bypassrootandsslpinning",
    "Q0120S/frida-detection-bypass",
    "c0desec/ssl-pinning-bypass",
    "c0desec/s-bypass",
    "ahrixia/root-detection-and-ssl-pinning-bypass",
    "HCIBO/mobil-framework-detect",
    "sdcampbell/android-inspect-webviews",
    "damaidec/root-detection-bypass-for-cordova-plugin-devicecompile",
    "sdcampbell/android-hook-crypto-functions",
    "sdcampbell/android-hook-notification-builder",
    "yorgundur0/androidsslbypass",
    "Anof-cyber/flutter-windows-ssl-pinning-bypass-",
    "axhlzy/fridadebugger",
    "axhlzy/il2cpphookscripts",
    "Q0120S/universal-root-detection-and-ssl-pinning-bypass",
    "S03HT3T/fridalab-solution-script",
    "0x25CBFC4F/firebase-for-android-react-native-dumper",
    "acsayson/rootandpinning",
    "d3tonator/ssl-and-root-detection-bypass",
    "hyugogirubato/android-ssl-pinning",
    "0xshdax/bypass-root-plugins-cyberkatze-iroot",
    "vicsanjinez/anti-root-and-ssl-pinning2",
    "bsxp/okhttp-logging",
    "fopina/piracy-checker-bypass",
    "hyugogirubato/android-java-interceptor",
    "ercu/okhttp-log-root",
    "ivan-sincek/android-ssl-pinning-bypass-2",
    "0xForp/anti-root-and-ssl-bypass-in-1",
    "ispiropoulos/root-and-ssl-bypass",
    "workwhileweb/ssl",
    "incogbyte/android-mix-sslunpin-bypass",
    "nmatt0/mysslunpin",
    "zeroinside/tracesslexceptions",
    "KishorBal/multiple-root-detection-bypass",
    "platix/get-android-security-provider-mstg-network-6",
    "gchib297/custom-phonegap-sslcertificatechecker-bypass",
    "yoavst/okhttp3-interceptor-obfuscated",
    "ninjadiary/frinja---sharedpreferences",
    "ninjadiary/frinja---permissions",
    "ninjadiary/frinja----java-io",
    "limyout/root-detection-and--ssl-pinning",
]


def build_command(codeshare: str, package_name: str) -> str:
    return f"frida -U -f {package_name} --codeshare {codeshare}"


def auto_confirm_prompt(line: str) -> bool:
    lowered = line.lower()
    indicators = ["[y/n]", "proceed?", "continue?", "confirm"]
    return any(ind in lowered for ind in indicators)


def prompt_yes_no(prompt: str, default: str = "n", timeout: float = 15.0) -> str:
    if not sys.stdin.isatty():
        print(f"Non-interactive input detected; using default '{default}'.")
        return default

    response: List[str] = [""]

    def ask() -> None:
        response[0] = input(prompt).strip().lower()

    thread = threading.Thread(target=ask, daemon=True)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print(f"No response received within {timeout} seconds; using default '{default}'.")
        return default

    if response[0] in {"y", "yes"}:
        return "y"
    if response[0] in {"n", "no"}:
        return "n"
    return default


def terminate_process(process: subprocess.Popen[str]) -> None:
    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)


def run_frida_command(command: str, package_name: str, dry_run: bool = False) -> bool:
    print(f"\n[{package_name}] Trying: {command}")
    if dry_run:
        print("Dry run enabled; skipping execution.\n")
        return False

    if shutil.which("frida") is None:
        print("Frida CLI was not found on PATH. Install Frida and try again.")
        return False

    process = subprocess.Popen(
        command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    output_lines: List[str] = []

    def stream_output() -> None:
        assert process.stdout is not None
        while True:
            line = process.stdout.readline()
            if not line:
                break
            cleaned = line.rstrip()
            output_lines.append(cleaned)
            if cleaned:
                print(cleaned)
            if auto_confirm_prompt(cleaned):
                try:
                    process.stdin.write("y\n")
                    process.stdin.flush()
                except Exception:
                    pass

    thread = threading.Thread(target=stream_output, daemon=True)
    thread.start()

    try:
        time.sleep(2)
        if process.stdin is not None:
            try:
                process.stdin.write("y\n")
                process.stdin.flush()
            except Exception:
                pass

        if process.poll() is not None:
            print("The Frida process exited immediately. This script likely failed to start.")
            return False

        while process.poll() is None:
            response = prompt_yes_no("Were you able to intercept the request with this script? [y/n]: ", default="n", timeout=10)
            if response in {"y", "yes"}:
                print(f"\n{GREEN}Successful script: {command}{RESET}")
                print(f"{GREEN}Frida session opened successfully for {package_name}.{RESET}")
                print("The session is running. Press Ctrl+C in this terminal to stop it.")
                try:
                    while process.poll() is None:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\nSession stopped by user.")
                return True
            if response in {"n", "no"}:
                break
            print("Please enter y or n.")

        terminate_process(process)
        return False
    except KeyboardInterrupt:
        print("\nInterrupted by user. Stopping the current Frida session.")
        terminate_process(process)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Try Frida bypass scripts one by one for a package")
    parser.add_argument("--package-name", help="Android/iOS package name to test")
    parser.add_argument("--dry-run", action="store_true", help="Show the commands without executing them")
    args = parser.parse_args()

    package_name = args.package_name or input("Enter the package name: ").strip()
    if not package_name:
        print("Package name cannot be empty.")
        sys.exit(1)

    commands = [build_command(codeshare, package_name) for codeshare in FRIDA_CODESHARES]
    if not commands:
        print("No Frida commands were configured.")
        sys.exit(1)

    print(f"Loaded {len(commands)} Frida script(s) from the built-in list")

    for index, command in enumerate(commands, start=1):
        print(f"\n=== Script {index}/{len(commands)} ===")
        if run_frida_command(command, package_name, dry_run=args.dry_run):
            return

    print(f"\n{GREEN}{package_name} is secured.{RESET}")


if __name__ == "__main__":
    main()
