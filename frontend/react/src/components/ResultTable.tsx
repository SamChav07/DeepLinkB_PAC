import React from 'react';
import styles from './ResultTable.module.css';

function ResultTable() {
  return (
    <div className={styles.tableContainer}>
      <div className={styles.tableWrapper} style={{ height: '500px', width: '100%' }}>
        {
        <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRYvb7FKhzN2VKqRQQNHoAzLL4qyn-w6fRRPEqfhlFS5U8f__DQNt_3UWVN71KfvJLIQcur5m7MT3Xi/pubhtml?gid=914413653&amp;single=true&amp;widget=true&amp;headers=false"
          width="100%"
          height="100%"
          frameBorder="0"
        ></iframe>
        }
      </div>
    </div>
  );
}

export default ResultTable;