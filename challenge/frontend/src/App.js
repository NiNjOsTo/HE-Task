import './App.css';
import React from 'react';
import { BrowserRouter,Routes, Route } from "react-router-dom";
import Packages from './Packages/Packages';
import DetailedPackage from './DetailedPackage/DetailedPackage';
function App() {

  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route index element={<Packages />} />
          <Route path="/package/:id" element={<DetailedPackage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
