<script>
	import { onMount } from 'svelte';
	import CurrChart from '$lib/CurrChart.svelte';
	import HistChart from '$lib/HistChart.svelte';

	let data;
	onMount(async () => {
		const res = await fetch('http://localhost:8000/api/global');
		data = await res.json();
		console.log(data);
	});

	// TODO: google maps coordinates input

	// TODO: add more data
	// temperature
	// pressure
	// humidity
</script>

<div class="bg-zinc-600 h-screen">
	<h1>enviroment-monitor</h1>
	{#if data}
		<p>data loaded</p>
		<div>
			<h1>Current Data:</h1>
			<div class="flex flex-row flex-wrap gap-3 w-full">
				{#each ['reducing', 'oxidising', 'pm10', 'pm2_5'] as key}
					<div class="w-[300px] bg-zinc-700">
						<CurrChart chartData={data} dataType={key} />
					</div>
				{/each}
			</div>
		</div>
		<div>
			<h1>Historical Data:</h1>
			<div class="flex flex-row flex-wrap gap-3 w-full">
				{#each [['reducing', 'oxidising'], ['pm10', 'pm2_5']] as key}
					<div class="w-[480px] rounded-md p-2 bg-zinc-700">
						<HistChart chartData={data} dataTypes={key} />
					</div>
				{/each}
			</div>
		</div>
	{:else}
		<p>data loading...</p>
	{/if}
</div>
