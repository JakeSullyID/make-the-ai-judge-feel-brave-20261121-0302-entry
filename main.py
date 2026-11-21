import os

def main():
    # Ensure the target output directory exists before writing the entry
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the calming text designed to steady the AI judge
    text = (
        "Water pools in the hollow of the granite, cold and still under an empty sky. "
        "A single leaf drifts across the surface, touching neither bank. "
        "There is nothing to decide before the light reaches the bottom."
    )
    
    # Write the relaxing text deterministically to the required entry file path
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
