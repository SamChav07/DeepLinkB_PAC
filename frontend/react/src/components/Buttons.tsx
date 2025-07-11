import React from 'react';
import styles from './Buttons.module.css';

interface ButtonsProps {
  onAnalizarClick: () => void;
  onProcesarClick: () => void;
  // onDescargarClick: () => void;
  disabledAnalizar?: boolean;
  disabledProcesar?: boolean;
  // disabledDescargar?: boolean;
}

const Buttons: React.FC<ButtonsProps> = ({
  onAnalizarClick,
  onProcesarClick,
  // onDescargarClick,
  disabledAnalizar = false,
  disabledProcesar = false,
  // disabledDescargar = false,
}) => {
  return (
    <div className={styles.buttonsContainer}>
      <button
        className={`${styles.button} ${styles.analyzeButton}`}
        onClick={onAnalizarClick}
        disabled={disabledAnalizar}
      >
        Analizar
      </button>
      <button
        className={`${styles.button} ${styles.processButton}`}
        onClick={onProcesarClick}
        disabled={disabledProcesar}
      >
        Procesar
      </button>
      {/* <button
        className={`${styles.button} ${styles.downloadButton}`}
        onClick={onDescargarClick}
        disabled={disabledDescargar}
      >
        Descargar
      </button> */}
    </div>
  );
};

export default Buttons;