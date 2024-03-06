<script>
	import { onMount } from 'svelte';
	import Chart from '$lib/Chart.svelte';

	let data;
	onMount(async () => {
		const res = await fetch('http://localhost:8000/api/global');
		data = await res.json();
		// console.log(data);
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
		<div class="flex flex-row flex-wrap gap-3 w-full max-w-[1000px]">
			{#each ['pm10', 'pm2_5', 'reducing', 'oxidising'] as key}
				<div class="w-[480px] rounded-md p-2 bg-zinc-700">
					<Chart chartData={data} dataType={key} />
				</div>
			{/each}
		</div>
	{:else}
		<p>data loading...</p>
	{/if}
</div>
