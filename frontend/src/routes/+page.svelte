<script>
	import { onMount } from 'svelte';
	import Chart from '../components/Chart.svelte';

	let data;
	onMount(async () => {
		const res = await fetch('http://localhost:8000/api/global');
		data = await res.json();
		// console.log(data);
	});
</script>

<h1>enviroment-monitor</h1>

<!-- <pre>
  {JSON.stringify(data, null, 2)}
</pre> -->

{#if data}
	<p>data loaded</p>
	<Chart chartData={data} dataType="pm10" />
	<Chart chartData={data} dataType="pm2_5" />
	<Chart chartData={data} dataType="oxidising" />
	<Chart chartData={data} dataType="reducing" />
{:else}
	<p>data loading...</p>
{/if}
