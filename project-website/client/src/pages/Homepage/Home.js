import styles from "./Home.module.css";
import Slideshow from "./../../components/UI/Slideshow";
import PageContent from "./PageContent";
import Header from "../../components/Layout/Header";
import { useEffect, useState } from "react";

const Home = () => {
  const [isTransparent, setIsTransparent] = useState(false);

  useEffect(() => {
    let selector = document.querySelector(`.${styles["scroll-container"]}`);
    selector.addEventListener("scroll", () => {
      console.log(selector.scrollTop);
      if (selector.scrollTop >= 900) setIsTransparent(true);
      else setIsTransparent(false);
    });
  }, []);

  return (
    <div className={styles["scroll-container"]}>
      <Header className={isTransparent ? "navbar-bg" : "hover-navbar"} />
      <Slideshow />
      <PageContent />
    </div>
  );
};

export default Home;
