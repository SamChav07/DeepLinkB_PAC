import { useState } from 'react';
import styles from './FileDrop.module.css';

interface FileDropProps {
  onFilesChange: (files: File[]) => void;
}

function FileDrop({ onFilesChange }: FileDropProps) {
  const [files, setFiles] = useState<File[]>([]);
  const [uploading, setUploading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const uploadFile = async (file: File) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://localhost:8000/api/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Error al subir el archivo");
      const data = await response.json();
      console.log("Archivo subido con éxito:", data);
    } catch (err) {
      console.error(err);
      setError("Fallo al subir el archivo.");
    }
  };

  const updateFiles = (newFilesList: File[]) => {
    setFiles(newFilesList);
    onFilesChange(newFilesList);

    // Subimos los archivos nuevos
    setUploading(true);
    Promise.all(newFilesList.map(uploadFile))
      .finally(() => setUploading(false));
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const newFiles = Array.from(e.dataTransfer.files);
    updateFiles([...files, ...newFiles]);
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newFiles = e.target.files ? Array.from(e.target.files) : [];
    updateFiles([...files, ...newFiles]);
  };

  const handleRemove = (indexToRemove: number) => {
    const updatedList = files.filter((_, idx) => idx !== indexToRemove);
    setFiles(updatedList);
    onFilesChange(updatedList);
  };

  return (
    <div>
      <div
        className={styles.dropZone}
        onDragOver={e => e.preventDefault()}
        onDrop={handleDrop}
      >
        📥 Arrastra tus archivos aquí o usa el botón para subir
      </div>

      <input type="file" multiple onChange={handleFileInput} className={styles.fileInput} />

      {uploading && <p className={styles.uploading}>Subiendo archivos...</p>}
      {error && <p className={styles.error}>{error}</p>}

      <ul className={styles.fileList}>
        {files.map((file, idx) => (
          <li key={idx} className={styles.fileItem}>
            <span className={styles.fileName}>{file.name}</span>
            <button
              type="button"
              onClick={() => handleRemove(idx)}
              aria-label={`Eliminar ${file.name}`}
              className={styles.removeButton}
            >
              ×
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default FileDrop;