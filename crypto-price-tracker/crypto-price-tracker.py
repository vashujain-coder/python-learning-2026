import requests
import os
import json
from datetime import datetime

FILENAME = "alerts.json"


def fetch_price(coin):
    """Fetch live price of a coin in INR. Returns float or None on error."""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": coin,
            "vs_currencies": "inr"
        }
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        data = r.json()
        if coin not in data:
            print(f"❌ '{coin.capitalize()}' not found. Check the coin name.")
            return None
        return round(float(data[coin]["inr"]), 2)
    except requests.exceptions.Timeout:
        print("⚠️  Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️  HTTP error: {e}")
    except requests.exceptions.ConnectionError:
        print("⚠️  No internet connection.")
    except Exception as e:
        print(f"⚠️  Unexpected error: {e}")
    return None


def get_price(coin):
    """Fetch and display the price of a single coin."""
    price = fetch_price(coin)
    if price is not None:
        print(f"  {coin.capitalize():<15} ₹{price:>15,.2f}")


def set_alert(coin, target_price, condition):
    """Save a new price alert to alerts.json."""
    alert = {
        "coin": coin,
        "target_price": target_price,
        "condition": condition,
        "created": datetime.now().strftime("%d/%m/%Y")
    }

    alerts = []
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                alerts = json.load(f)
        except Exception as e:
            print(f"⚠️  Error loading alerts: {e}")

    alerts.append(alert)

    try:
        with open(FILENAME, "w") as f:
            json.dump(alerts, f, indent=4)
        print(f"✅ Alert set — {coin.capitalize()} "
              f"{'above' if condition == 'Above' else 'below'} "
              f"₹{target_price:,.2f}")
    except Exception as e:
        print(f"⚠️  Error saving alert: {e}")


def view_alerts():
    """Display all saved price alerts."""
    if not os.path.exists(FILENAME):
        print("❌ No alerts found.")
        return

    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"⚠️  Error loading alerts: {e}")
        return

    if not data:
        print("❌ No alerts found.")
        return

    print("\n" + "=" * 70)
    print(f"  {'Coin':<15} {'Target (₹)':>14} {'Condition':<10} {'Created'}")
    print("=" * 70)
    for alert in data:
        print(f"  {alert['coin'].capitalize():<15} "
              f"₹{alert['target_price']:>13,.2f} "
              f"{alert['condition']:<10} "
              f"{alert['created']}")
    print("=" * 70)
    print(f"  {len(data)} alert(s) total.\n")


def check_alert():
    """Check all saved alerts against live prices and notify if triggered."""
    if not os.path.exists(FILENAME):
        return

    try:
        with open(FILENAME, "r") as f:
            alerts = json.load(f)
    except Exception as e:
        print(f"⚠️  Error loading alerts: {e}")
        return

    if not alerts:
        return

    print("\n🔍 Checking alerts...")
    triggered = 0
    for alert in alerts:
        price = fetch_price(alert["coin"])
        if price is None:
            continue

        if alert["condition"] == "Above" and price > alert["target_price"]:
            print(f"🚨 ALERT: {alert['coin'].capitalize()} is ₹{price:,.2f} "
                  f"— above your target of ₹{alert['target_price']:,.2f}!")
            triggered += 1

        elif alert["condition"] == "Below" and price < alert["target_price"]:
            print(f"🚨 ALERT: {alert['coin'].capitalize()} is ₹{price:,.2f} "
                  f"— below your target of ₹{alert['target_price']:,.2f}!")
            triggered += 1

    if triggered == 0:
        print("✅ No alerts triggered.")


def run():
    """Main menu loop."""
    supported_coins = [
        "Bitcoin", "Ethereum", "Dogecoin",
        "Solana", "Binancecoin", "Ripple"
    ]

    while True:
        print("\n💰 Crypto Price Tracker 💰\n")
        print("=" * 50)
        print("  1. Check Crypto Price")
        print("  2. Set Price Alert")
        print("  3. View Alert History")
        print("  4. Check Alerts Now")
        print("  5. Exit")
        print("=" * 50)

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\nSupported coins: " + ", ".join(supported_coins))
            user_input = input("\nEnter coin(s) — single or comma separated: ")
            coin_list = [c.strip().lower() for c in user_input.split(",")]
            print()
            for coin in coin_list:
                if coin.capitalize() in supported_coins:
                    get_price(coin)
                else:
                    print(f"❌ '{coin.capitalize()}' not in supported list.")

        elif choice == "2":
            while True:
                print("\nSupported coins: " + ", ".join(supported_coins))
                coin = input("\nEnter coin: ").strip().lower()
                if coin.capitalize() in supported_coins:
                    break
                print(f"❌ '{coin.capitalize()}' not in supported list.")

            while True:
                try:
                    target = round(float(input("\nEnter target price (₹): ")), 2)
                    if target <= 0:
                        print("❌ Price must be positive!")
                        continue
                    break
                except ValueError:
                    print("❌ Please enter a valid number!")

            while True:
                condition = input("\nCondition (Above / Below): ").strip().capitalize()
                if condition in ["Above", "Below"]:
                    break
                print("❌ Please type 'Above' or 'Below'.")

            set_alert(coin, target, condition)

        elif choice == "3":
            view_alerts()

        elif choice == "4":
            check_alert()

        elif choice in ["5", "exit"]:
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    check_alert()
    run()