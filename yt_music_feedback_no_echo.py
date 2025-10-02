from pynput import keyboard 
import json 
import os
from ytmusicapi import YTMusic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Global variables
ytmusic = None
driver = None

def start_browser():
    """Start Fiprint("\n📋 Instructions:")
print(" - Press F1 to 👍 LIKE the cur# Ask user if they want to use browser scraping
if not# Initialize YouTube Music API
api_co# Initialize YouTube Music API
api_connecprint("\n📋 Instructions:")
print(" - Press F1 to 👍 LIKE the current song (clicks thumbs up on YouTube Music)")
print(" - Press F2 to 👎 DISLIKE the current song (clicks thumbs down on YouTube Music)")  
print(" - Press ESC to exit the program")

# Show current mode
if driver:
    print(" - 🌐 Browser mode: Active - F1/F2 will click YouTube Music buttons!")
    print(" - 💡 Make sure YouTube Music tab is open and logged in")
elif api_connected:
    print(" - 🔑 API mode: Active (saving feedback only, no button clicking)")
else:
    print(" - 🧪 Test mode: Active (saving fake feedback only)")

print("\n🎯 Click away from this window, then use F1/F2 while listening to music!")
print("   Your keyboard shortcuts will automatically rate songs on YouTube Music!")e_ytmusic()

# Always ask user about browser mode (for button clicking)
print("\n🌐 Browser Mode Options:")
if api_connected:
    print("   ✅ YouTube Music API is connected")
    print("   🎯 Browser mode will let you click actual thumbs up/down buttons")
else:
    print("   ❌ No API connection available")
    print("   🎯 Browser mode is needed for song detection and button clicking")

choice = input("\nStart Firefox to click YouTube Music buttons? (y/n): ").lower().strip()
if choice == 'y':
    browser_started = start_browser()
    if browser_started:
        print("✅ Browser mode enabled - Firefox is running")
        print("📖 Please navigate to a song on YouTube Music and try F1/F2")
        
        # Wait a moment for user to navigate, then test buttons
        print("\n⏳ Waiting 10 seconds for you to navigate to a song...")
        time.sleep(10)
        test_button_clicking()
    else:
        print("❌ Browser failed to start - using API/test mode only")
else:
    print("📝 Browser mode disabled - using API/test mode only")
print(" - Press F1 to 👍 LIKE the current song (clicks thumbs up on YouTube Music)")
print(" - Press F2 to 👎 DISLIKE the current song (clicks thumbs down on YouTube Music)")  
print(" - Press ESC to exit the program")

# Show current mode
if driver:
    print(" - 🌐 Browser mode: Active - F1/F2 will click YouTube Music buttons!")
    print(" - 💡 Make sure YouTube Music tab is open and logged in")
elif api_connected:
    print(" - 🔑 API mode: Active (saving feedback only, no button clicking)")
else:
    print(" - 🧪 Test mode: Active (saving fake feedback only)")

print("\n🎯 Click away from this window, then use F1/F2 while listening to music!")
print("   Your keyboard shortcuts will automatically rate songs on YouTube Music!")lize_ytmusic()

# Always ask user about browser mode (for button clicking)
print("\n🌐 Browser Mode Options:")
if api_connected:
    print("   ✅ YouTube Music API is connected")
    print("   🎯 Browser mode will let you click actual thumbs up/down buttons")
else:
    print("   ❌ No API connection available")
    print("   🎯 Browser mode is needed for song detection and button clicking")

choice = input("\nStart Firefox to click YouTube Music buttons? (y/n): ").lower().strip()
if choice == 'y':
    browser_started = start_browser()
    if browser_started:
        print("✅ Browser mode enabled - Firefox is running")
        print("📖 Please navigate to a song on YouTube Music and try F1/F2")
        
        # Wait a moment for user to navigate, then test buttons
        print("\n⏳ Waiting 10 seconds for you to navigate to a song...")
        time.sleep(10)
        test_button_clicking()
    else:
        print("❌ Browser failed to start - using API/test mode only")
else:
    print("📝 Browser mode disabled - using API/test mode only")ed:
    print("\n🌐 No API connection. Would you like to use browser mode for button clicking?")
    choice = input("Start Firefox to click YouTube Music buttons? (y/n): ").lower().strip()
    if choice == 'y':
        browser_started = start_browser()
        if browser_started:
            print("✅ Browser method enabled - Firefox is running")
            print("📖 Please navigate to a song on YouTube Music and try F1/F2")
            
            # Wait a moment for user to navigate, then test buttons
            print("\n⏳ Waiting 10 seconds for you to navigate to a song...")
            time.sleep(10)
            test_button_clicking()
        else:
            print("❌ Browser failed to start - using test mode")
    else:
        print("📝 Using test mode only")licks thumbs up on YouTube Music)")
print(" - Press F2 to 👎 DISLIKE the current song (clicks thumbs down on YouTube Music)")  
print(" - Press ESC to exit the program")

# Show current mode
if driver:
    print(" - 🌐 Browser mode: Active - F1/F2 will click YouTube Music buttons!")
    print(" - 💡 Make sure YouTube Music tab is open and logged in")
elif api_connected:
    print(" - 🔑 API mode: Active (saving feedback only, no button clicking)")
else:
    print(" - 🧪 Test mode: Active (saving fake feedback only)")

print("\n🎯 Click away from this window, then use F1/F2 while listening to music!")
print("   Your keyboard shortcuts will automatically rate songs on YouTube Music!")YouTube Music"""
    global driver
    try:
        # Try different possible locations for geckodriver
        possible_paths = [
            "C:\\Users\\knigh\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe",
            "C:\\Users\\knigh\\Downloads\\geckodriver.exe",
            "geckodriver.exe",  # If it's in PATH
            "geckodriver"       # If it's in PATH without .exe
        ]
        
        service = None
        for path in possible_paths:
            if os.path.exists(path) or path in ["geckodriver.exe", "geckodriver"]:
                try:
                    service = Service(path)
                    break
                except:
                    continue
        
        if not service:
            # Try without specifying path (if geckodriver is in PATH)
            service = Service()
        
        driver = webdriver.Firefox(service=service)
        driver.get("https://music.youtube.com")
        print("🌐 Firefox started - log in to YouTube Music if needed")
        time.sleep(5)  # Wait for the page to load
        return True
        
    except Exception as e:
        print(f"❌ Error starting browser: {e}")
        print("   Possible solutions:")
        print("   1. Download geckodriver from https://github.com/mozilla/geckodriver/releases")
        print("   2. Place geckodriver.exe in your Downloads folder")
        print("   3. Or add geckodriver to your system PATH")
        return False

def initialize_ytmusic():
    """Initialize YouTube Music API"""
    global ytmusic
    try:
        # Check multiple possible locations for headers_auth.json
        auth_paths = [
            "headers_auth.json",  # Current directory
            "c:\\Users\\knigh\\headers_auth.json",  # Where setup script created it
            os.path.join(os.path.expanduser("~"), "headers_auth.json")  # Home directory
        ]
        
        auth_file = None
        for path in auth_paths:
            if os.path.exists(path):
                auth_file = path
                break
                
        if auth_file:
            ytmusic = YTMusic(auth_file)
            print(f"✅ YouTube Music API connected! (using {auth_file})")
            return True
        else:
            print("❌ headers_auth.json not found in any expected location!")
            print("   Expected locations:")
            for path in auth_paths:
                print(f"   - {path}")
            print("   For now, using test mode...")
            return False
    except Exception as e:
        print(f"❌ Error connecting to YouTube Music: {e}")
        print("   Using test mode...")
        return False

def get_current_song():
    """Grab current song info from YouTube Music page"""
    global driver
    try:
        if not driver:
            return {"title": "No Browser", "artist": "No Browser", "videoId": "N/A"}
            
        # Locate song title and artist elements (updated selectors for YouTube Music)
        try:
            title_elem = driver.find_element(By.CSS_SELECTOR, '.title.ytmusic-player-bar')
            title = title_elem.text.strip()
        except Exception:
            try:
                title_elem = driver.find_element(By.CSS_SELECTOR, '[class*="title"]')
                title = title_elem.text.strip()
            except Exception:
                title = "Unknown Title"

        # Get artist
        try:
            artist_elem = driver.find_element(By.CSS_SELECTOR, '.byline.ytmusic-player-bar')
            artist = artist_elem.text.strip()
        except Exception:
            try:
                artist_elem = driver.find_element(By.CSS_SELECTOR, '[class*="byline"]')
                artist = artist_elem.text.strip()
            except Exception:
                artist = "Unknown Artist"

        # Get videoId from URL
        video_id = "N/A"
        try:
            current_url = driver.current_url
            if "watch?v=" in current_url:
                video_id = current_url.split("v=")[-1].split("&")[0]
            elif "/watch/" in current_url:
                video_id = current_url.split("/watch/")[-1].split("?")[0]
        except Exception:
            pass

        return {"title": title, "artist": artist, "videoId": video_id}
    
    except Exception as e:
        print(f"❌ Error getting current song: {e}")
        return {"title": "Unknown", "artist": "Unknown", "videoId": "N/A"}

def click_thumbs_up():
    """Click the thumbs up button on YouTube Music"""
    global driver
    if not driver:
        print("❌ No browser available to click thumbs up")
        return False
        
    try:
        # YouTube Music thumbs up button selectors (try multiple in case layout changes)
        like_selectors = [
            'button[aria-label*="Like"]',
            'button[title*="Like"]',
            '.like-button-renderer button',
            'tp-yt-paper-icon-button[aria-label*="Like"]',
            'ytmusic-like-button-renderer button',
            '[data-title="I like this"]',
            'button[aria-label="Like this song"]'
        ]
        
        button_clicked = False
        for selector in like_selectors:
            try:
                button = driver.find_element(By.CSS_SELECTOR, selector)
                if button.is_enabled() and button.is_displayed():
                    driver.execute_script("arguments[0].click();", button)
                    print("👍 Clicked thumbs up on YouTube Music!")
                    button_clicked = True
                    break
            except Exception:
                continue
                
        if not button_clicked:
            print("⚠️ Could not find thumbs up button to click")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error clicking thumbs up: {e}")
        return False

def click_thumbs_down():
    """Click the thumbs down button on YouTube Music"""  
    global driver
    if not driver:
        print("❌ No browser available to click thumbs down")
        return False
        
    try:
        # YouTube Music thumbs down button selectors
        dislike_selectors = [
            'button[aria-label*="Dislike"]',
            'button[title*="Dislike"]', 
            '.dislike-button-renderer button',
            'tp-yt-paper-icon-button[aria-label*="Dislike"]',
            'ytmusic-dislike-button-renderer button',
            '[data-title="I dislike this"]',
            'button[aria-label="Dislike this song"]'
        ]
        
        button_clicked = False
        for selector in dislike_selectors:
            try:
                button = driver.find_element(By.CSS_SELECTOR, selector)
                if button.is_enabled() and button.is_displayed():
                    driver.execute_script("arguments[0].click();", button)
                    print("� Clicked thumbs down on YouTube Music!")
                    button_clicked = True
                    break
            except Exception:
                continue
                
        if not button_clicked:
            print("⚠️ Could not find thumbs down button to click")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error clicking thumbs down: {e}")
        return False

# --- Save feedback function ---
def save_feedback(song_info, liked):
    # Use a specific directory for the JSON file
    feedback_file = os.path.join(os.path.expanduser("~"), "youtube_music_feedback.json")
    
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),  # Add timestamp
        "title": song_info.get("title"), # Song title
        "artist": song_info.get("artist"), # Song artist
        "videoId": song_info.get("videoId"), # YouTube video ID
        "liked": liked # Liked status
    }

    # Load existing feedback if file exists
    if os.path.exists(feedback_file): # Check if feedback file exists
        with open(feedback_file, "r") as f: # Open file in read mode
            data = json.load(f) # Load existing data
    else:
        data = [] # Initialize empty list if file doesn't exist

    # Add new entry
    data.append(entry) # Append new feedback entry

    #Save back to file
    with open(feedback_file, "w") as f: # Open file in write mode
        json.dump(data, f, indent=4) # Write updated data to file

    print(f"{'👍' if liked else '👎'} {entry['title']} - {entry['artist']} saved!")
    
    # Show file location on first save
    if len(data) == 1:  # First entry
        print(f"📁 Feedback saved to: {feedback_file}")
        
def show_feedback_location():
    """Show where the feedback JSON file is located"""
    feedback_file = os.path.join(os.path.expanduser("~"), "youtube_music_feedback.json")
    print(f"📁 Your feedback will be saved to:")
    print(f"   {feedback_file}")
    
    if os.path.exists(feedback_file):
        try:
            with open(feedback_file, "r") as f:
                data = json.load(f)
            print(f"📊 Current file has {len(data)} feedback entries")
        except Exception:
            print("⚠️ File exists but may be corrupted")
    else:
        print("📝 File will be created when you save your first feedback")
    print()

def open_feedback_folder():
    """Open the folder containing the feedback file"""
    import subprocess
    feedback_dir = os.path.expanduser("~")
    try:
        subprocess.Popen(f'explorer "{feedback_dir}"')
        print(f"📂 Opened folder: {feedback_dir}")
    except Exception as e:
        print(f"❌ Could not open folder: {e}")

# --- Handle key press events with selective suppression ---
def on_press(key):
    try:
        if key == keyboard.Key.f1: # If F1 key is pressed
            print("🎵 F1 pressed - Liking song...")
            
            # Get current song info first
            song_info = {"title": "Unknown", "artist": "Unknown", "videoId": "N/A"}
            if driver:  # If browser is running
                song_info = get_current_song()
                # Click the thumbs up button on YouTube Music
                if click_thumbs_up():
                    # Save feedback after successful click
                    save_feedback(song_info, liked=True)
                else:
                    print("⚠️ Could not click thumbs up, but saving feedback anyway")
                    save_feedback(song_info, liked=True)
            elif ytmusic:  # If API is connected
                song_info = {"title": "API Song", "artist": "API Artist", "videoId": "api123"}
                save_feedback(song_info, liked=True)
                print("👍 Feedback saved (API mode - no browser clicking)")
            else:
                song_info = {"title": "Test Song", "artist": "Test Artist", "videoId": "12345"}
                save_feedback(song_info, liked=True)
                print("👍 Feedback saved (Test mode)")
            
        elif key == keyboard.Key.f2: # If F2 key is pressed
            print("🎵 F2 pressed - Disliking song...")
            
            # Get current song info first
            song_info = {"title": "Unknown", "artist": "Unknown", "videoId": "N/A"}
            if driver:  # If browser is running
                song_info = get_current_song()
                # Click the thumbs down button on YouTube Music
                if click_thumbs_down():
                    # Save feedback after successful click
                    save_feedback(song_info, liked=False)
                else:
                    print("⚠️ Could not click thumbs down, but saving feedback anyway")
                    save_feedback(song_info, liked=False)
            elif ytmusic:  # If API is connected
                song_info = {"title": "API Song", "artist": "API Artist", "videoId": "api123"}
                save_feedback(song_info, liked=False)
                print("👎 Feedback saved (API mode - no browser clicking)")
            else:
                song_info = {"title": "Test Song", "artist": "Test Artist", "videoId": "12345"}
                save_feedback(song_info, liked=False)
                print("👎 Feedback saved (Test mode)")
            
        elif key == keyboard.Key.esc: # ESC to exit
            print("Exiting...")
            cleanup_browser()
            return False # Stop the listener
            
    except AttributeError:
        pass

def test_button_clicking():
    """Test if we can find and interact with YouTube Music buttons"""
    global driver
    if not driver:
        print("❌ No browser available for button testing")
        return
        
    print("🧪 Testing YouTube Music button detection...")
    
    try:
        # Test finding thumbs up button
        like_selectors = [
            'button[aria-label*="Like"]',
            'button[title*="Like"]',
            '.like-button-renderer button',
            'tp-yt-paper-icon-button[aria-label*="Like"]',
            'ytmusic-like-button-renderer button'
        ]
        
        like_found = False
        for selector in like_selectors:
            try:
                button = driver.find_element(By.CSS_SELECTOR, selector)
                if button.is_displayed():
                    print(f"✅ Found thumbs up button: {selector}")
                    like_found = True
                    break
            except Exception:
                continue
                
        if not like_found:
            print("⚠️ Could not find thumbs up button")
            
        # Test finding thumbs down button
        dislike_selectors = [
            'button[aria-label*="Dislike"]',
            'button[title*="Dislike"]', 
            '.dislike-button-renderer button',
            'tp-yt-paper-icon-button[aria-label*="Dislike"]',
            'ytmusic-dislike-button-renderer button'
        ]
        
        dislike_found = False
        for selector in dislike_selectors:
            try:
                button = driver.find_element(By.CSS_SELECTOR, selector)
                if button.is_displayed():
                    print(f"✅ Found thumbs down button: {selector}")
                    dislike_found = True
                    break
            except Exception:
                continue
                
        if not dislike_found:
            print("⚠️ Could not find thumbs down button")
            
        if like_found and dislike_found:
            print("🎉 Button detection successful! F1/F2 should work.")
        else:
            print("⚠️ Some buttons not found. Make sure you're on a song page.")
            
    except Exception as e:
        print(f"❌ Error testing buttons: {e}")

def cleanup_browser():
    """Clean up browser resources"""
    global driver
    try:
        if driver:
            driver.quit()
            print("🌐 Browser closed")
    except Exception as e:
        print(f"⚠️ Error closing browser: {e}")

# --- Start listener with NO suppression ---
print("🎵 YouTube Music Feedback Tracker")
print("=" * 40)

# Show where feedback will be saved
show_feedback_location()

# Initialize YouTube Music API
api_connected = initialize_ytmusic()

# Ask user if they want to use browser scraping
if not api_connected:
    print("\n🌐 No API connection. Would you like to use browser scraping?")
    choice = input("Start Firefox for song detection? (y/n): ").lower().strip()
    if choice == 'y':
        browser_started = start_browser()
        if browser_started:
            print("✅ Browser method enabled - Firefox is running")
        else:
            print("❌ Browser failed to start - using test mode")
    else:
        print("� Using test mode only")

print("\n�📋 Instructions:")
print(" - press F1 to 👍 like a song")
print(" - press F2 to 👎 dislike a song")
print(" - Press ESC to exit")

# Show current mode
if driver:
    print(" - 🌐 Browser mode: Active (scraping from Firefox)")
elif api_connected:
    print(" - 🔑 API mode: Active (using YouTube Music API)")
else:
    print(" - 🧪 Test mode: Active (fake song data)")

print("\n🎯 Click away from this window and use F1/F2!")
print()

try:
    # Use suppress=False to ensure we don't interfere with normal keyboard flow
    with keyboard.Listener(on_press=on_press, suppress=False) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n⏹️ Stopped by user")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Try running as administrator if issues persist.")
finally:
    cleanup_browser()

# Test API call only if connected (after main loop ends)
if api_connected and ytmusic:
    try:
        print("\n🧪 Testing API call...")
        search_results = ytmusic.search("test", limit=1)
        if search_results:
            print(f"✅ API test successful! Found: {search_results[0].get('title', 'Unknown')}")
        else:
            print("⚠️ API call worked but no results found")
    except Exception as e:
        print(f"⚠️ API test failed: {e}")
        print("   This is normal - basic functionality should still work")
else:
    print("\n💡 API test skipped - not using API mode")

# Ask if user wants to see their feedback file
feedback_file = os.path.join(os.path.expanduser("~"), "youtube_music_feedback.json")
if os.path.exists(feedback_file):
    print(f"\n📊 Your feedback file is located at:")
    print(f"   {feedback_file}")
    
    choice = input("\nWould you like to open the folder containing your feedback file? (y/n): ").lower().strip()
    if choice == 'y':
        open_feedback_folder()

print("\n👋 Goodbye!")