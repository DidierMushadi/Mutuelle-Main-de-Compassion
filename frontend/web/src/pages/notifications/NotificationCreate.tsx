export default function NotificationCreate() {
  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">
        Créer une notification
      </h1>

      <form className="space-y-4 max-w-md">
        <input
          className="w-full border p-2 rounded"
          placeholder="Titre"
          required
        />

        <textarea
          className="w-full border p-2 rounded"
          placeholder="Message"
          required
        />

        <button className="bg-green-600 text-white px-4 py-2 rounded">
          Envoyer
        </button>
      </form>
    </div>
  );
}
