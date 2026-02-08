import logo from "../assets/logo.png";

export default function Header() {
  return (
    <header
      style={{
        display: "flex",
        alignItems: "center",
        padding: "12px 24px",
        backgroundColor: "#0f172a",
        color: "#ffffff"
      }}
    >
      <img
        src={logo}
        alt="Mutuelle UMOJA"
        style={{ height: 48, marginRight: 16 }}
      />
      <h1 style={{ fontSize: 20, margin: 0 }}>
        Mutuelle Main de Compassion UMOJA
      </h1>
    </header>
  );
}
