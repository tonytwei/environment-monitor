<script>
    import Toggle from '$lib/Toggle.svelte';
    import Dial from '$lib/Dial.svelte';

    let data;

    fetch("http://localhost:8000/api/global", {
      method: "GET",
      headers: {
        accept: "application/json",
      },
      cache: "no-store",
    })
        .then((res) => data = res.json())
        .catch((error) => {
            console.log("Error fetching data:", error);
            throw new Error('Failed to fetch data');
        }); 
</script>

<h1>enviroment-monitor</h1>
{#if data}
    <h1>data</h1>
{:else}
    <Toggle />
    <Dial />
{/if}