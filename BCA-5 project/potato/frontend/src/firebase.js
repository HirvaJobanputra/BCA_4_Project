import { initializeApp } from "firebase/app";
import { getAuth,GoogleAuthProvider  } from "firebase/auth";


const firebaseConfig = {
apiKey: "AIzaSyB73r97NiTKrWzV4JralXrwpKJfzPV8Tzw",
  authDomain: "potato-eb67f.firebaseapp.com",
  projectId: "potato-eb67f",
  storageBucket: "potato-eb67f.firebasestorage.app",
  messagingSenderId: "130908298250",
  appId: "1:130908298250:web:397d59b59a10ad1912d3f3"
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const googleProvider = new GoogleAuthProvider();