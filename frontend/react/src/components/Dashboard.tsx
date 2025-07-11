import React, { useState } from 'react';
import FileDrop from './FileDrop';
import ResultTable from './ResultTable';
import Buttons from './Buttons';

interface AnalysisResult {
  archivo: string;
  autor: string;
  facultad: string;
  categoria: string;
  referencia: string;
  estado: string;
  fuente: string;
  url: string;
}

function Dashboard() {
  const [filesSubidos, setFilesSubidos] = useState<File[]>([]);
  const [resultados, setResultados] = useState<AnalysisResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFilesFromDropzone = (files: File[]) => {
    setFilesSubidos(files);
    setResultados([]); // Limpiar resultados previos si se suben nuevos archivos
  };

  const handleAnalizarClick = async () => {
    setLoading(true);
    setError(null);

    try {
      const res = await fetch('http://127.0.0.1:8000/api/analizar-todos/');
      if (!res.ok) throw new Error('Error al analizar los archivos.');
      const data: AnalysisResult[] = await res.json();
      setResultados(data);
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Fallo en la conexión con el servidor de análisis.');
    } finally {
      setLoading(false);
    }
  };

  const handleProcesarClick = async () => {
    setLoading(true);
    setError(null);

    try {
      const res = await fetch('http://127.0.0.1:8000/api/procesar-pendientes/');
      if (!res.ok) throw new Error('Error al procesar pendientes.');
      const data = await res.json();
      console.log('Procesamiento completado:', data);
      alert('Procesamiento completado correctamente.');
    } catch (err: any) {
      console.error(err);
      setError(err.message || 'Fallo en la conexión con el servidor de procesamiento.');
    } finally {
      setLoading(false);
    }
  };

  // const handleDescargarClick = () => {
  //   if (resultados.length === 0) {
  //     setError('No hay resultados para descargar.');
  //     return;
  //   }

  //   alert('Función de descarga aún no implementada.');
  //   // Ejemplo real si existiera:
  //   // window.open('http://127.0.0.1:8000/api/descargar-resultados');
  // };

  return (
    <div className="dashboard-container" style={{ padding: '20px', maxWidth: '1200px', margin: 'auto' }}>
      <h1>Sistema de Gestión de Documentos</h1>

      {error && (
        <div style={{ color: 'red', marginBottom: '10px', background: '#ffe6e6', padding: '10px', borderRadius: '5px' }}>
          {error}
        </div>
      )}

      <h2>1. Subir Archivos</h2>
      <FileDrop onFilesChange={handleFilesFromDropzone} />

      <h2>2. Acciones</h2>
      <Buttons
        onAnalizarClick={handleAnalizarClick}
        onProcesarClick={handleProcesarClick}
        // onDescargarClick={handleDescargarClick}
        disabledAnalizar={filesSubidos.length === 0 || loading}
        disabledProcesar={loading}
        // disabledDescargar={resultados.length === 0}
      />

      {loading && <p style={{ color: '#007bff', marginTop: '10px' }}>Cargando, por favor espera...</p>}

      <h2>3. Resultados</h2>
      <ResultTable results={resultados} />
    </div>
  );
}

export default Dashboard;