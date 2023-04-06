// console.log("yo");
// async function downloadFile() {
//   console.log("hei");
//   // make an AJAX request to fetch the data from the API endpoint
//   const response = await fetch("/contacts/vcard");
//   const data = await response.json();

//   // create a blob with the data
//   const blob = new Blob([JSON.stringify(data)], { type: "text/vcard" });

//   // create a download link for the blob
//   const url = URL.createObjectURL(blob);

//   // create a link element and click it to start the download
//   const link = document.createElement("a");
//   link.href = url;
//   link.download = "data.json";
//   document.body.appendChild(link);
//   link.click();

//   // cleanup the URL object
//   URL.revokeObjectURL(url);
// }
