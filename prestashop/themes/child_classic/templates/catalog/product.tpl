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
                  <a class="nav-link" data-toggle="tab" href="#product-delivery" role="tab" aria-controls="product-delivery">
                    {l s='Koszty dostawy' d='Shop.Theme.Catalog'}
                  </a>
                </li>

                <!-- Nowa zakładka 2 -->
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#product-opinions" role="tab" aria-controls="product-opinions">
                    {l s='Opinie' d='Shop.Theme.Catalog'}
                  </a>
                </li>
              </ul>
              <!-- Opis produktu -->

              <div class="tab-content" id="tab-content">
                <div class="tab-pane fade in{if $product.description} active js-product-tab-active{/if}" id="description"
                  role="tabpanel">
                  {block name='product_description'}
                    <div class="product-description">{$product.description nofilter}</div>
                  {/block}
                </div>

                {block name='product_details'}
                  {include file='catalog/_partials/product-details.tpl'}
                {/block}

                {foreach from=$product.extraContent item=extra key=extraKey}
                  <div class="tab-pane fade in {$extra.attr.class}" id="extra-{$extraKey}" role="tabpanel"
                    {foreach $extra.attr as $key => $val} {$key}="{$val}" {/foreach}>
                    {$extra.content nofilter}
                  </div>
                {/foreach}
                <!-- Koszty dostawy -->
                <div class="tab-pane fade" id="product-delivery" role="tabpanel">
                  <div class="product-delivery">
                    <div class="innerbox tab-content product-deliveries">
                      <div class="delivery-container" id="deliveries">
                        <div class="shipping-country-select" style="display: none;">
                          <span>
                            <em>Kraj wysyłki:</em>
                          </span>

                          <span>
                            <select name="shipping-country" class="shipping-country"></select>
                          </span>
                        </div>

                        <div class="shippings " data-cost-from="od" data-cost-free="Darmowa">
                          <div class="shipping row f-row">
                            <div class="shipping-label-container f-grid-9"><span class="shipping-label">InPost Paczkomaty
                                24/7</span></div>
                            <div class="shipping-cost f-grid-3">9,99&nbsp;zł</div>
                          </div>
                          <div class="shipping row f-row">
                            <div class="shipping-label-container f-grid-9"><span class="shipping-label">Kurier DPD - dostawa
                                do punktu</span></div>
                            <div class="shipping-cost f-grid-3">11,99&nbsp;zł</div>
                          </div>
                          <div class="shipping row f-row">
                            <div class="shipping-label-container f-grid-9"><span class="shipping-label">Orlen Paczka</span>
                            </div>
                            <div class="shipping-cost f-grid-3">11,99&nbsp;zł</div>
                          </div>
                          <div class="shipping row f-row">
                            <div class="shipping-label-container f-grid-9"><span class="shipping-label">InPost Kurier</span>
                            </div>
                            <div class="shipping-cost f-grid-3">14,99&nbsp;zł</div>
                          </div>
                          <div class="shipping row f-row">
                            <div class="shipping-label-container f-grid-9"><span class="shipping-label">Kurier DPD</span>
                            </div>
                            <div class="shipping-cost f-grid-3">16,99&nbsp;zł</div>
                          </div>
                          <div class="shipping row f-row">
                            <div class="shipping-label-container f-grid-9"><span class="shipping-label">Kurier DHL</span>
                            </div>
                            <div class="shipping-cost f-grid-3">17,99&nbsp;zł</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Opinie -->
                <div class="tab-pane fade" id="product-opinions" role="tabpanel">
                  {hook h='displayFooterProduct' product=$product category=$category}
                </div>

              {block name='product_attachments'}
                {if $product.attachments}
                  <div class="tab-pane fade in" id="attachments" role="tabpanel">
                    <section class="product-attachments">
                      <p class="h5 text-uppercase">{l s='Download' d='Shop.Theme.Actions'}</p>
                      {foreach from=$product.attachments item=attachment}
                        <div class="attachment">
                          <h4><a
                              href="{url entity='attachment' params=['id_attachment' => $attachment.id_attachment]}">{$attachment.name}</a>
                          </h4>
                          <p>{$attachment.description}</p>
                          <a href="{url entity='attachment' params=['id_attachment' => $attachment.id_attachment]}">
                            {l s='Download' d='Shop.Theme.Actions'} ({$attachment.file_size_formatted})
                          </a>
                        </div>
                      {/foreach}
                    </section>
                  </div>
                {/if}
              {/block}
            </div>
          {/block}
        </div>
      {/block}
    </div>

  </section>
{/block}