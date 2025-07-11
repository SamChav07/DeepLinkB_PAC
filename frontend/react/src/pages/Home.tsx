import Dashboard from '../components/Dashboard';
import styles from './Home.module.css';

function Home() {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>📚 BiblioPDFs</h1>
      <Dashboard />
    </div>
  );
}

export default Home;