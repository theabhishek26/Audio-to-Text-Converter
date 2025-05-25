import assemblyai as aai
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os
from flask import Flask, request, jsonify, render_template

# Load environment variables
load_dotenv()

# Configure AssemblyAI API key
AAI_API_KEY = os.getenv("AAI_API_KEY")
aai.settings.api_key = AAI_API_KEY

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# Create upload directory if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        # File validation (removed language check)
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
            
        file = request.files["file"]
        
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400
            
        if file:
            # Secure and save file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            
            # Verify audio file
            if not filename.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')):
                os.remove(filepath)
                return jsonify({"error": "Unsupported file type"}), 400

            try:
                # Transcribe with AssemblyAI
                transcriber = aai.Transcriber()
                transcript = transcriber.transcribe(filepath)
                
                if transcript.status == aai.TranscriptStatus.error:
                    os.remove(filepath)
                    return jsonify({"error": f"Transcription failed: {transcript.error}"}), 500
                
                # Return only the transcription (removed translation part)
                os.remove(filepath)
                return jsonify({
                    "transcript": transcript.text
                })
                
            except Exception as e:
                if os.path.exists(filepath):
                    os.remove(filepath)
                return jsonify({"error": str(e)}), 500
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)