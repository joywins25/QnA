<script>
  const target_url = "http://127.0.0.1:8000/hi";
  
  async function hello() {
  try {
    const resp = await fetch(target_url);
    if (resp.ok) {
      // response is ok, parse as JSON
      const json = await resp.json();
      return json.message;
    } else {
      // response is not ok, throw an error
      throw new Error(`방법0201Error :  HTTP error ${resp.status}`);
    }
  } catch (error) {
    console.log(error);
    return `방법0202Error : Error fetching data : ${error}`;
  }
  }

  let promise = hello();
</script>

{#await promise}
  <p>...waiting</p>
{:then message}
  <h1>{message}</h1>
{/await}
