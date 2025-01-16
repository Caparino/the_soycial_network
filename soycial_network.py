from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
import os
import argparse


def capture_screenshot_with_playwright(screenshot_path, linkedin_embed_url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 500, 'height': 800}  # Set both width and height
        )
        page = context.new_page()
        
        # Go to the embed URL
        page.goto(linkedin_embed_url)
        
        # Wait for any content to load
        page.wait_for_selector('body', state='visible')
        # Give extra time for dynamic content to load
        page.wait_for_timeout(5000)
        
        # Take screenshot of full page
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot successfully captured.")
        browser.close()

def overlay_images(screenshot_path, overlay_image_path, output_image_path):
    try:
        # Open the LinkedIn post screenshot and the overlay image
        base_image = Image.open(screenshot_path).convert("RGBA")

        # Create a black box for censoring
        black_color = (0, 0, 0, 255)  # RGBA black
        draw = ImageDraw.Draw(base_image)
        
        # Draw black rectangles for censoring
        # Profile picture (coordinates based on sample images)
        draw.rectangle([(15, 15), (65, 65)], fill=black_color)
        
        # Name and title area (coordinates based on sample images)
        draw.rectangle([(70, 15), (475, 50)], fill=black_color)
        
        overlay_image = Image.open(overlay_image_path).convert("RGBA")

        # Get base image dimensions
        base_width, base_height = base_image.size
        
        # Crop out the bottom comment section and side borders
        border_size = 2  # Adjust this value based on the border width
        cropped_height = base_height - 60  # Remove approximately 60 pixels from bottom
        base_image = base_image.crop((
            border_size,  # Left crop
            0,           # Top crop
            base_width - border_size,  # Right crop
            cropped_height  # Bottom crop
        ))
        
        # Get new base dimensions after crop
        base_width, base_height = base_image.size
        
        # Make overlay width match the base width exactly
        overlay_width = base_width
        aspect_ratio = overlay_image.size[1] / overlay_image.size[0]
        overlay_height = int(overlay_width * aspect_ratio)
        
        # Resize overlay proportionally
        overlay_image = overlay_image.resize((overlay_width, overlay_height))

        # Calculate position to align closer to bottom
        position = (
            0,  # Left align
            base_height - overlay_height,  # Adjust the +50 to move soyjaks up or down
        )

        # Paste the overlay image on top of the base image
        base_image.paste(overlay_image, position, overlay_image)

        # Save the final image
        base_image.save(output_image_path)
        print(f"Final image saved as {output_image_path}")
    except Exception as e:
        print(f"Error occurred while overlaying images: {e}")


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Create a meme from a LinkedIn post')
    parser.add_argument('linkedin_embed_url', help='The LinkedIn embed URL to screenshot')
    args = parser.parse_args()

    # Paths for images
    screenshot_path = "linkedin_post_screenshot.png"
    overlay_image_path = "soyjaks_pointing_overlay.png"
    output_image_path = "output.png"

    # Capture screenshot
    capture_screenshot_with_playwright(screenshot_path, args.linkedin_embed_url)

    # Overlay images
    overlay_images(screenshot_path, overlay_image_path, output_image_path)

    # Clean up the screenshot
    os.remove(screenshot_path)

if __name__ == "__main__":
    main()