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
<div class="product-add-to-cart js-product-add-to-cart">
  {if !$configuration.is_catalog}

    <script type="text/javascript">
      document.addEventListener("DOMContentLoaded", function() {
        var quantityInput = document.getElementById('quantity_wanted');
        var addToCartButton = document.getElementById('add-to-cart-btn');

        function checkQuantity() {
          var enteredQuantity = parseInt(quantityInput.value);
          if (enteredQuantity > {$product.quantity}) {
          addToCartButton.disabled = true;
        } else {
          addToCartButton.disabled = false;
        }
      }

      quantityInput.addEventListener('input', checkQuantity);

      checkQuantity();
      });
    </script>


    {block name='product_quantity'}
      <div class="product-quantity clearfix">
        {if $product.quantity > 0}

          <div class="add">
            <form action="{$urls.pages.cart}" method="POST" class="main-page-add-to-cart add-to-cart-or-refresh">
              <div class="product-number-div">
                <div class="qty">
                  <input type="number" name="qty" id="quantity_wanted" inputmode="numeric" pattern="[0-9]*"
                    value="{if $product.quantity_wanted}{$product.quantity_wanted}{else}1{/if}"
                    min="{if $product.quantity_wanted}{$product.minimal_quantity}{else}1{/if}" class="input-group"
                    aria-label="{l s='Quantity' d='Shop.Theme.Actions'}">
                </div>
                <span class="control-label szt-class">{l s='szt.' d='Shop.Theme.Catalog'}</span>
              </div>
              <input type="hidden" name="token" value="{$static_token}">
              <input type="hidden" name="id_product" value="{$product.id}">

              <button class="btn btn-primary add-to-cart product-page-add-to-cart" id="add-to-cart-btn"
                data-button-action="add-to-cart" type="submit" {if !$product.add_to_cart_url} disabled {/if}>
                {l s='Do koszyka' d='Shop.Theme.Actions'}
              </button>
            </form>
          </div>

          {hook h='displayProductActions' product=$product}
        {else}
          <div class="button_wrap">
            <button type="submit" onclick="window.location.href='/kontakt';"
              class="non-availability-notifier-btn btn btn-red">
              <span>powiadom o dostępności</span>
            </button>
          </div>
        {/if}
      </div>
    {/block}

    {block name='product_availability'}
      <span id="product-availability" class="js-product-availability">
        {if $product.show_availability && $product.availability_message}
          {if $product.availability == 'available'}
            <i class="material-icons rtl-no-flip product-available">&#xE5CA;</i>
          {elseif $product.availability == 'last_remaining_items'}
            <i class="material-icons product-last-items">&#xE002;</i>
          {else}
            <p class="towar-niedostepny">towar niedostępny</p>
          {/if}
        {/if}
      </span>
    {/block}

    {block name='product_minimal_quantity'}
      <p class="product-minimal-quantity js-product-minimal-quantity">
        {if $product.minimal_quantity > 1}
          {l
                                  s='The minimum purchase order quantity for the product is %quantity%.'
                                  d='Shop.Theme.Checkout'
                                  sprintf=['%quantity%' => $product.minimal_quantity]
                                  }
        {/if}
      </p>
    {/block}
  {/if}
</div>