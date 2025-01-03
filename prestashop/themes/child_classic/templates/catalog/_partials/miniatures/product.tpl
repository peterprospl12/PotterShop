{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}
{block name='product_miniature_item'}
  <div class="js-product product{if !empty($productClasses)} {$productClasses}{/if}">
  <article class="product-miniature js-product-miniature {if $product.quantity <= 0}inactive-miniature{/if}" data-id-product="{$product.id_product}"
      data-id-product-attribute="{$product.id_product_attribute}">
      <div class="thumbnail-container">
        <div class="thumbnail-top">
          {block name='product_thumbnail'}
            {if $product.cover}
              <a href="{$product.url}" class="thumbnail product-thumbnail">
                <img src="{$product.cover.bySize.home_default.url}"
                  alt="{if !empty($product.cover.legend)}{$product.cover.legend}{else}{$product.name|truncate:30:'...'}{/if}"
                  loading="lazy" data-full-size-image-url="{$product.cover.large.url}"
                  width="{$product.cover.bySize.home_default.width}" height="{$product.cover.bySize.home_default.height}" />
              </a>
            {else}
              <a href="{$product.url}" class="thumbnail product-thumbnail">
                <img src="{$urls.no_picture_image.bySize.home_default.url}" loading="lazy"
                  width="{$urls.no_picture_image.bySize.home_default.width}"
                  height="{$urls.no_picture_image.bySize.home_default.height}" />
              </a>
            {/if}
          {/block}

          <div class="product-description">
            {block name='product_name'}
              {if $page.page_name == 'index'}
                <h3 class="h3 product-title"><a href="{$product.url}"
                    content="{$product.url}">{$product.name|truncate:30:'...'}</a></h3>
              {else}
                <h2 class="h3 product-title"><a href="{$product.url}"
                    content="{$product.url}">{$product.name|truncate:30:'...'}</a></h2>
              {/if}
            {/block}

            <div class="miniature-price-and-button">
              {block name='product_price_and_shipping'}
                {if $product.show_price}
                  <div class="product-price-and-shipping">

                    {hook h='displayProductPriceBlock' product=$product type="before_price"}

                    <span class="price" aria-label="{l s='Price' d='Shop.Theme.Catalog'}">
                      {capture name='custom_price'}{hook h='displayProductPriceBlock' product=$product type='custom_price' hook_origin='products_list'}{/capture}
                      {if '' !== $smarty.capture.custom_price}
                        {$smarty.capture.custom_price nofilter}
                      {else}
                        {$product.price}
                      {/if}
                    </span>

                    {if $product.has_discount}
                      {hook h='displayProductPriceBlock' product=$product type="old_price"}

                      <span class="regular-price"
                        aria-label="{l s='Regular price' d='Shop.Theme.Catalog'}">{$product.regular_price}</span>
                      {if $product.discount_type === 'percentage'}
                        <span class="discount-percentage discount-product">{$product.discount_percentage}</span>
                      {elseif $product.discount_type === 'amount'}
                        <span class="discount-amount discount-product">{$product.discount_amount_to_display}</span>
                      {/if}
                    {/if}

                    {hook h='displayProductPriceBlock' product=$product type='unit_price'}

                    {hook h='displayProductPriceBlock' product=$product type='weight'}
                  </div>
                {/if}
              {/block}

              {block name='product_reviews'}
                {hook h='displayProductListReviews' product=$product}
                {if !$configuration.is_catalog}
                  {if $product.customization_required === false}
                    {if $product.quantity >= 1}
                      <form action="{$urls.pages.cart}" method="POST" class="main-page-add-to-cart add-to-cart-or-refresh">
                        <input type="hidden" name="token" value="{$static_token}">
                        <input type="hidden" name="id_product" value="{$product.id}">
                        <input type="hidden" name="qty" value="1">
                        <button class="btn btn-primary add-to-cart custom-button-add-to-cart" data-button-action="add-to-cart"
                          type="submit" {if $product.quantity < 1}disabled{/if}>
                          {l s='DO KOSZYKA' d='Shop.Theme.Actions'}
                        </button>
                      </form>
                    {else}
                      <div class="button_wrap">
                        <button type="submit" onclick="window.location.href='/kontakt';"
                          class="custom-button-add-to-cart-disabled btn btn-red" data-is-logged="false" data-stock-id="572"
                          data-product-id="422" data-product-name="Harry Potter Lampka Hedwiga">
                          <span>powiadom o dostępności</span>
                        </button>
                      </div>
                    {/if}
                  {else}

                  {/if}
                {/if}
              {/block}
            </div>
          </div>

          {include file='catalog/_partials/product-flags.tpl'}
        </div>
    </article>
  </div>
{/block}