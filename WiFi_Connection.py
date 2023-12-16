import subprocess

def connect_to_wifi(ssid, password):
    try:
        # Use nmcli (NetworkManager command-line tool) to connect to the Wi-Fi network
        subprocess.run(['nmcli', 'device', 'wifi', 'connect', ssid, 'password', password], check=True)
        print(f"Connected to Wi-Fi network: {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to connect to Wi-Fi network - {e}")

if __name__ == "__main__":
    # Replace 'your_wifi_ssid' and 'your_wifi_password' with your actual Wi-Fi credentials
    wifi_ssid = 'your_wifi_ssid'
    wifi_password = 'your_wifi_password'

    connect_to_wifi(wifi_ssid, wifi_password)
