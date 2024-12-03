<div class="product-slider owl-carousel">
    {foreach from=$products item=product}
        <div class="product-item">
            <a href="{$product.link}" title="{$product.name}">
                <img src="{$product.cover.bySize.home_default.url}" alt="{$product.name}" />
                <h3>{$product.name}</h3>
                <p>{$product.price|price_format}</p>
            </a>
        </div>
    {/foreach}
</div>
