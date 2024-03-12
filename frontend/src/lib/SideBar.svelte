<script>
	import info from '$lib/assets/info.png';
	import melbourne from '$lib/assets/melbourne.png';
	import sydney from '$lib/assets/sydney.png';
	import london from '$lib/assets/london.png';
	import new_york from '$lib/assets/new_york.png';
	import paris from '$lib/assets/paris.png';
	import rio from '$lib/assets/rio.png';
	import tokyo from '$lib/assets/tokyo.png';
	import beijing from '$lib/assets/beijing.png';

	export let showInfo;
	export let loading;
	export let location;

	const cityImages = [melbourne, sydney, london, new_york, paris, rio, tokyo, beijing];
	const imageLocationMap = {
		[melbourne]: 'Melbourne',
		[sydney]: 'Sydney',
		[london]: 'London',
		[new_york]: 'New York',
		[paris]: 'Paris',
		[rio]: 'Rio de Janeiro',
		[tokyo]: 'Tokyo',
		[beijing]: 'Beijing'
	};
</script>

<div class="bg-zinc-700 w-min h-[calc(100vh-80px)]">
	{#each cityImages as image}
		<button
			on:click={() => {
				location = imageLocationMap[image];
				loading = true;
				showInfo = false;
			}}
			class={`p-2 w-max ${imageLocationMap[image] == location ? 'bg-purple-600' : ''}`}
		>
			<img src={image} alt="city" class="w-16 invert" />
		</button>
	{/each}
	<button
		on:click={() => {
			location = '';
			showInfo = true;
		}}
		class={`flex items-center justify-center align-middle p-4 ${
			showInfo == true ? 'bg-purple-600' : ''
		}`}
	>
		<img src={info} alt="show info" class="w-14 invert" />
	</button>
</div>
