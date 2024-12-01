{extends file=$layout}

{block name="left_column"}
  <div id="left-column" class="col-xs-12 col-sm-4 col-md-3 product-page-left-column">
    {if $page.page_name == 'product'}
      <div class="custom-boxhead">
        <span>Producenci</span>
      </div>
      <div class="producers_wrap">
        <select class="manufacturers-select" onchange="redirectToManufacturer(this)">
          <option label="Wybierz" value="">wybierz</option>
          {foreach from=$manufacturers item=manufacturer}
            <option value="{$link->getManufacturerLink($manufacturer.id_manufacturer)|escape:'html':'UTF-8'}">
              {$manufacturer.name|escape:'html':'UTF-8'}
            </option>
          {/foreach}
        </select>

        <script>
          function redirectToManufacturer(selectElement) {
            const url = selectElement.value;
            if (url) {
              window.location.href = url;
            }
          }
        </script>
      </div>
    {else}
      {hook h="displayLeftColumn"}
    {/if}
  </div>
{/block}

{block name='head' append}
  <meta property="og:type" content="product">
  {if $product.cover}
    <meta property="og:image" content="{$product.cover.large.url}">
  {/if}

  {if $product.show_price}
    <meta property="product:pretax_price:amount" content="{$product.price_tax_exc}">
    <meta property="product:pretax_price:currency" content="{$currency.iso_code}">
    <meta property="product:price:amount" content="{$product.price_amount}">
    <meta property="product:price:currency" content="{$currency.iso_code}">
  {/if}
  {if isset($product.weight) && ($product.weight != 0)}
    <meta property="product:weight:value" content="{$product.weight}">
    <meta property="product:weight:units" content="{$product.weight_unit}">
  {/if}
{/block}

{block name='head_microdata_special'}
  {include file='_partials/microdata/product-jsonld.tpl'}
{/block}

{block name='content'}

  <section id="main">
    <meta content="{$product.url}">

    <div class="row product-container js-product-container">
      {***************    heading with product name   ***************}
      <div class="product-boxhead">
        {block name='page_header_container'}
          {block name='page_header'}
            <h1 class="h1">{block name='page_title'}{$product.name}{/block}</h1>
          {/block}
        {/block}
      </div>
      {***************    left column   ***************}
      <div class="full-width-row">
        <div class="innerbox">
          <div class="col-md-6">
            {block name='page_content_container'}
              <section class="page-content" id="content">
                {block name='page_content'}
                  {include file='catalog/_partials/product-flags.tpl'}

                  {block name='product_cover_thumbnails'}
                    {include file='catalog/_partials/product-cover-thumbnails.tpl'}
                  {/block}
                  <div class="scroll-box-arrows">
                    <i class="material-icons left">&#xE314;</i>
                    <i class="material-icons right">&#xE315;</i>
                  </div>

                {/block}
              </section>
            {/block}
          </div>
          {***************    right column   ***************}
          <div class="col-md-6">
            <div class="product-page-header">
              <div class="product-page-header-row">
                <span class="first">Dostępność:</span>
                <span class="second">
                  {block name='product_quantities'}
                    {if $product.show_quantities}
                      <div class="product-quantities">
                        <label class="xddd">{l s='In stock' d='Shop.Theme.Catalog'}</label>
                        <span data-stock="{$product.quantity}"
                          data-allow-oosp="{$product.allow_oosp}">{*({$product.quantity})*}</span>
                      </div>
                    {/if}
                  {/block}
                </span>
              </div>
              <div class="product-page-header-row">
                <span class="first">Wysyłka w:</span>
                <span class="second">24 godziny</span>
              </div>
              <div class="product-page-header-row">
                <span class="first">Dostawa:</span>
                <span class="second">Darmowa</span>
                <a href="1-czas-i-koszty-dostawy" title="sprawdź formy dostawy">
                  <span>sprawdź formy dostawy</span>
                </a>
              </div>
            </div>
            {block name='product_prices'}
              {include file='catalog/_partials/product-prices.tpl'}
            {/block}

            {block name='product_variants'}
              {include file='catalog/_partials/product-variants.tpl'}
            {/block}

            {block name='product_add_to_cart'}
              {include file='catalog/_partials/product-add-to-cart.tpl'}
            {/block}

            {*Ocena custom*}

            <div class="product-rate-stars">
              <div class="vote-message-row">
                <em class="vote-message">Ocena:</em>
                <span class="votestars" id="votestars_48">
                  <img src="/img/star.svg" alt="" class="px1 star0">
                  <img src="/img/star.svg" alt="" class="px1 star0">
                  <img src="/img/star.svg" alt="" class="px1 star0">
                  <img src="/img/star.svg" alt="" class="px1 star0">
                  <img src="/img/star.svg" alt="" class="px1 star0">
                </span>
              </div>
            </div>
            <div class="product-share">
              <ul class="row-links-q">
                <li class="question">
                  <a href="/zapytaj-o-produkt" title="zapytaj o produkt" class="question">
                    <span>zapytaj o produkt</span>
                  </a>
                </li>
                <li class="mailfriend">
                  <a href="/udostepnij-znajomemu" title="poleć znajomemu" class="mailfriend">
                    <span>poleć znajomemu</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      {************************}
      {block name='product_footer'}
        <div class="product-information">
          {block name='product_tabs'}
            <div class="tabs">
              <ul class="nav nav-tabs" role="tablist">
                {if $product.description}
                  <li class="nav-item">
                    <a class="nav-link{if $product.description} active js-product-nav-active{/if}" data-toggle="tab"
                      href="#description" role="tab" aria-controls="description" {if $product.description} aria-selected="true"
                      {/if}>
                      {l s='Description' d='Shop.Theme.Catalog'}
                    </a>
                  </li>
                {/if}

                <!-- Nowa zakładka 1 -->
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#custom-tab1" role="tab" aria-controls="custom-tab1">
                    {l s='Koszty dostawy' d='Shop.Theme.Catalog'}
                  </a>
                </li>

                <!-- Nowa zakładka 2 -->
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#custom-tab2" role="tab" aria-controls="custom-tab2">
                    {l s='Opinie' d='Shop.Theme.Catalog'}
                  </a>
                </li>

                <!-- Nowa zakładka 3 -->
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#custom-tab3" role="tab" aria-controls="custom-tab3">
                    {l s='Produkty powiązane' d='Shop.Theme.Catalog'}
                  </a>
                </li>
              </ul>
            </div>
          {/block}
        </div>
      {/block}
    </div>

  </section>
{/block}