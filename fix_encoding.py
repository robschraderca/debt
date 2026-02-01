import os

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'rb') as f:
            content = f.read()
        
        original = content
        
        # Replace the mojibake bytes
        # â†' in UTF-8 is: c3 a2 e2 80 a0 27 (when double-encoded)
        bad_arrow = bytes([0xc3, 0xa2, 0xe2, 0x80, 0xa0, 0x27])
        good_arrow = bytes([0xe2, 0x86, 0x92])  # → in UTF-8
        content = content.replace(bad_arrow, good_arrow)
        
        # Try another variant: â†'
        bad_arrow2 = "â†'".encode('utf-8')
        content = content.replace(bad_arrow2, good_arrow)
        
        # Fix bullet: â— 
        bad_bullet = "â—".encode('utf-8')
        good_bullet = bytes([0xe2, 0x97, 0x8f])  # ● in UTF-8
        content = content.replace(bad_bullet, good_bullet)
        
        if content != original:
            with open(filename, 'wb') as f:
                f.write(content)
            print(f"Fixed: {filename}")
        else:
            print(f"No changes: {filename}")
