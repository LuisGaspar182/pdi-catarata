import os
import glob
import subprocess

RAW_DIR = "data/raw_videos"
OUT_DIR = "data/preprocessed"

FPS = 10  # taxa de extração de frames


def extract_frames(video_path):
    """Extrai frames de um vídeo para uma pasta com o nome do vídeo."""
    
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = os.path.join(OUT_DIR, video_name)

    # Cria a pasta se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Comando ffmpeg
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps={FPS}",
        f"{output_folder}/frame_%06d.png"
    ]

    print(f"\nProcessando vídeo: {video_name}")
    print("Salvando frames em:", output_folder)

    # Executa o FFmpeg
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def process_all_videos():
    """Processa todos os vídeos dentro de data/raw_videos/."""
    
    videos = glob.glob(os.path.join(RAW_DIR, "*.mp4"))

    if not videos:
        print("Nenhum vídeo encontrado em data/raw_videos/")
        return

    print(f"\nEncontrados {len(videos)} vídeos para processar.")
    
    for video in videos:
        extract_frames(video)

    print("\nProcesso concluído com sucesso!")


if __name__ == "__main__":
    process_all_videos()
